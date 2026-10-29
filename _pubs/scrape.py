"""Find SALSA publications in OpenAlex and write candidates.yml.

Each entry in candidates.yml is one version of a paper: an arXiv preprint and
its published version are separate entries with their own dates, so each can
be reported in the period it appeared. candidates.yml is regenerated on every
run; put manual decisions in decisions.yml.

Usage:  python _pubs/scrape.py
Set OPENALEX_API_KEY in the environment to use an OpenAlex API key.
"""

import datetime as dt
import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PIS_FILE = HERE / "pis.yml"
OUT_FILE = HERE / "candidates.yml"

OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works/"
ARXIV = "http://export.arxiv.org/api/query"
USER_AGENT = "salsa-pubs/1.0 (+https://github.com/sdrangan/sdrangan.github.io)"

ARXIV_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})|10\.48550/arxiv\.(\d{4}\.\d{4,5})", re.I)


def get(url, params=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code != 429 and e.code < 500:
                raise
        except urllib.error.URLError:
            pass
        time.sleep(2 ** attempt * 3)
    raise RuntimeError(f"failed to fetch {url}")


def fetch_works(author_ids, since):
    params = {
        "filter": f"author.id:{'|'.join(author_ids)},from_publication_date:{since}",
        "select": "id,doi,title,publication_date,type,primary_location,locations,authorships",
        "per-page": 200,
        "cursor": "*",
    }
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    works = []
    while params["cursor"]:
        page = json.loads(get(OPENALEX, params))
        works += page["results"]
        params["cursor"] = page["meta"].get("next_cursor")
    return works


def short_name(name):
    """'Sundeep Rangan' -> 'S. Rangan'; leaves names that are already short."""
    parts = name.split()
    if len(parts) < 2:
        return name
    first = [p if p.endswith(".") else p[0] + "." for p in parts[:-1]]
    return " ".join(first + [parts[-1]])


def bare_doi(doi):
    return doi.lower().removeprefix("https://doi.org/") if doi else None


def arxiv_id(work):
    for loc in work["locations"]:
        for url in (loc.get("landing_page_url"), loc.get("pdf_url")):
            m = ARXIV_RE.search(url or "")
            if m:
                return m.group(1) or m.group(2)
    m = ARXIV_RE.search(work.get("doi") or "")
    return (m.group(1) or m.group(2)) if m else None


def product_type(work):
    if work["type"] == "conference-paper":
        return "Conference"
    if work["type"] == "dataset":
        return "Dataset"
    source = (work.get("primary_location") or {}).get("source") or {}
    if work["type"] == "article" and source.get("type") == "journal":
        return "Journal"
    if work["type"] == "article" and source.get("type") == "conference":
        return "Conference"
    return "Other"


def published_versions(work, pi_by_id):
    """Split one OpenAlex work into its published and preprint versions."""
    title = (work.get("title") or "").strip()
    authors = ", ".join(short_name(a["author"]["display_name"]) for a in work["authorships"])
    pis = sorted({pi_by_id[a["author"]["id"].rsplit("/", 1)[-1]]
                  for a in work["authorships"]
                  if a["author"].get("id") and a["author"]["id"].rsplit("/", 1)[-1] in pi_by_id})
    common = {"title": title, "authors": authors, "pis": pis,
              "openalex": work["id"].rsplit("/", 1)[-1]}

    versions = []
    axid = arxiv_id(work)
    doi = bare_doi(work.get("doi"))
    if doi and not doi.startswith("10.48550/arxiv"):
        source = (work.get("primary_location") or {}).get("source") or {}
        versions.append({
            "id": f"doi:{doi}",
            **common,
            "type": product_type(work),
            "venue": source.get("display_name") or "",
            "date": work["publication_date"],
            "date_source": "openalex",
            "url": f"https://doi.org/{doi}",
        })
    if axid:
        versions.append({
            "id": f"arxiv:{axid}",
            **common,
            "type": "Preprint",
            "venue": f"arXiv preprint arXiv:{axid}",
            "date": work["publication_date"] if not versions else None,
            "date_source": "openalex",
            "url": f"https://arxiv.org/abs/{axid}",
        })
    if not versions:
        versions.append({
            "id": f"openalex:{common['openalex']}",
            **common,
            "type": product_type(work),
            "venue": ((work.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
            "date": work["publication_date"],
            "date_source": "openalex",
            "url": work["id"],
        })
    return versions


def merge(entries):
    """Merge entries with the same id, keeping the fullest record."""
    merged = {}
    for e in entries:
        old = merged.get(e["id"])
        if old is None:
            merged[e["id"]] = e
            continue
        old["pis"] = sorted(set(old["pis"]) | set(e["pis"]))
        if e.get("related"):
            old["related"] = sorted(set(old.get("related", [])) | set(e["related"]))
        for k in ("venue", "date"):
            if not old.get(k) and e.get(k):
                old[k] = e[k]
        if len(e["authors"]) > len(old["authors"]):
            old["authors"] = e["authors"]
    return list(merged.values())


def link_versions(entries):
    """Record the preprint/published pairs found in the same OpenAlex work."""
    by_work = {}
    for e in entries:
        by_work.setdefault(e["openalex"], []).append(e["id"])
    for e in entries:
        others = [i for i in by_work[e["openalex"]] if i != e["id"]]
        if others:
            e["related"] = sorted(set(e.get("related", [])) | set(others))


def crossref_date(doi):
    """Earliest full publication date Crossref has for a DOI, as (date, source).

    Many IEEE records give only the year; then the DOI registration date
    ('created', close to when the paper went online) is used instead.
    """
    body = get(CROSSREF + urllib.parse.quote(doi))
    if not body:
        return None, None
    msg = json.loads(body)["message"]
    dates = []
    for key in ("published-online", "published-print", "published", "issued"):
        parts = (msg.get(key) or {}).get("date-parts", [[None]])[0]
        if len(parts) == 3 and parts[0]:
            dates.append(dt.date(*parts))
    if dates:
        return min(dates).isoformat(), "crossref"
    parts = (msg.get("created") or {}).get("date-parts", [[None]])[0]
    if len(parts) == 3:
        return dt.date(*parts).isoformat(), "crossref registration"
    return None, None


def arxiv_dates(ids):
    """Date each arXiv ID was first posted (v1)."""
    out = {}
    ns = {"a": "http://www.w3.org/2005/Atom"}
    ids = sorted(ids)
    for i in range(0, len(ids), 100):
        body = get(ARXIV, {"id_list": ",".join(ids[i:i + 100]), "max_results": 100})
        for entry in ET.fromstring(body).findall("a:entry", ns):
            m = re.search(r"abs/(\d{4}\.\d{4,5})", entry.findtext("a:id", "", ns))
            published = entry.findtext("a:published", "", ns)
            if m and published:
                out[m.group(1)] = published[:10]
        time.sleep(3)
    return out


def fix_dates(entries):
    for e in entries:
        kind, key = e["id"].split(":", 1)
        if kind == "doi" and (not e["date"] or e["date"].endswith("-01-01")):
            d, source = crossref_date(key)
            if d:
                e["date"], e["date_source"] = d, source
            else:
                e["date_note"] = "year only; check the date"
    posted = arxiv_dates(e["id"].split(":", 1)[1] for e in entries if e["id"].startswith("arxiv:"))
    for e in entries:
        axid = e["id"].removeprefix("arxiv:")
        if axid in posted:
            e["date"], e["date_source"] = posted[axid], "arxiv"
        elif e["id"].startswith("arxiv:") and not e["date"]:
            yymm = axid.split(".")[0]
            e["date"] = f"20{yymm[:2]}-{yymm[2:]}-01"
            e["date_source"] = "arxiv id"


def default_awards(entry, pis, awards):
    """Awards of the entry's PIs that had started by the entry's date."""
    out = set()
    for name in entry["pis"]:
        for a in pis[name]["awards"]:
            if entry["date"] and entry["date"] >= str(awards[a]["start"]):
                out.add(a)
    return sorted(out)


def main():
    cfg = yaml.safe_load(PIS_FILE.read_text(encoding="utf-8"))
    pis = {p["name"]: p for p in cfg["pis"]}
    pi_by_id = {aid: p["name"] for p in cfg["pis"] for aid in p["openalex_ids"]}
    since = min(str(a["start"]) for a in cfg["awards"].values())

    works = fetch_works(list(pi_by_id), since)
    print(f"{len(works)} works from OpenAlex")

    entries = [v for w in works for v in published_versions(w, pi_by_id)]
    link_versions(entries)
    entries = merge(entries)
    fix_dates(entries)
    for e in entries:
        e["awards"] = default_awards(e, pis, cfg["awards"])
    entries = [e for e in entries if e["awards"]]
    entries.sort(key=lambda e: (e["date"] or "", e["id"]), reverse=True)

    keys = ["id", "title", "authors", "type", "venue", "date", "date_source",
            "date_note", "url", "pis", "awards", "related", "openalex"]
    entries = [{k: e[k] for k in keys if k in e} for e in entries]
    header = (f"# Generated by scrape.py on {dt.date.today()}. Do not edit; "
              "put decisions in decisions.yml.\n")
    OUT_FILE.write_text(header + yaml.safe_dump(entries, sort_keys=False, allow_unicode=True, width=1000),
                        encoding="utf-8")
    print(f"{len(entries)} entries written to {OUT_FILE.name}")


if __name__ == "__main__":
    main()
