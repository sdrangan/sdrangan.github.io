# SALSA product lists for NTIA reports

Builds the NOFO-1 (36-60-IF003) and NOFO-2 (36-60-IF2419) product
spreadsheets for each six-month performance report. Reports are due for
periods ending **3/31** and **9/30**.

Jekyll ignores this folder (it starts with `_`), so nothing here appears on
the website.

## Files

| File | Who edits it | What it holds |
|---|---|---|
| `pis.yml` | you | PIs with OpenAlex IDs and awards; award names and start dates; **the report period** |
| `candidates.yml` | `scrape.py` | every paper found in OpenAlex. **Never edit**: it is overwritten on each scrape |
| `decisions.yml` | you | per-paper decisions: which award, exclude, corrections, late items |
| `products.yml` | you | products that are not papers: datasets, software, talks, testbeds, patents |
| `scrape.py` | | finds papers in OpenAlex, fixes dates from Crossref and arXiv |
| `build.py` | | writes the spreadsheets to `output/` and lists papers needing review |

Needs Python with `pyyaml` and `openpyxl` (`pip install pyyaml openpyxl`).
Run the commands from the repo root.

## Each report, step by step

### 1. Set the report period

In `pis.yml`, change the `report` dates to the new six-month period:

```yaml
report:
  start: 2026-10-01
  end: 2027-03-31
```

If personnel changed, update the `pis` list too. A new PI needs their
OpenAlex ID: search for them at [openalex.org](https://openalex.org)
(choose **Authors**) and copy the `A...` ID from the profile URL. List every
profile if their papers are split across several.

### 2. Scrape

```
python _pubs/scrape.py
```

Takes about a minute. It rewrites `candidates.yml` with all PI papers since
the awards started. Your decisions are kept, since they are in
`decisions.yml`.

### 3. Build and see what needs review

```
python _pubs/build.py
```

It writes the spreadsheets and ends with a list of the papers in the period
that are **not yet in `decisions.yml`**. Those are included with their default
awards (the awards of the PIs on the paper), which is often wrong for
papers by PIs on both awards (Rangan, Rahmani, Dhananjay).

### 4. Decide on each paper in the review list

Add each one to `decisions.yml`, using the id from the list:

```yaml
"arxiv:2604.02498":
  award: nofo2        # nofo1 | nofo2 | both | exclude | default
```

- `exclude`: not SALSA work (other grants, other topics, supplementary files).
- `default`: you checked it and the scraped awards are right.
- Optionally fix a scraped field: `title`, `authors`, `venue`, `type`, `url`,
  `date`. Add `note:` for your own reminder; it is not written out.

Look up any paper's details in `candidates.yml` by searching for its id.

### 5. Add items that were missed

- **A paper from an earlier period that was never reported:** add
  `report: <this report's end date>` to its entry in `decisions.yml`.
- **A paper the scrape did not find** (OpenAlex had not indexed it yet, or
  did not link a PI to it): add it to `products.yml` with type `Journal`,
  `Conference` or `Preprint`.
- Skim `candidates.yml` against your own list of recent papers, since a paper
  whose only PI was not recognized by OpenAlex will be missing.

### 6. Add products that are not papers

Add them to `products.yml`. Each needs a `title`, `type`, `date` and
`award` (`nofo1`, `nofo2` or `both`); `venue`, `authors` and `url` are
optional. Its date decides which report it goes in (or set `report:`).

```yaml
- title: "FR3 multi-band channel measurement dataset"
  type: Dataset
  date: 2026-11-15
  award: nofo2
  venue: "IEEE DataPort"
  url: https://example.org/dataset
```

Things to collect from the team: datasets, code releases, invited talks,
tutorials, demos, testbed milestones, patents and invention disclosures,
standards contributions.

### 7. Rebuild until the review list is empty

```
python _pubs/build.py
```

Repeat steps 4–6 until it prints no review list and no warnings.

### 8. Check and submit

Open the two files in `output/`:

- `NYU IF003 NOFO-1 products <end date>.xlsx`
- `NYU IF2419 NOFO-2 products <end date>.xlsx`

Check the titles, dates and venues, then submit them with the report.

### 9. Commit

Commit `pis.yml`, `candidates.yml`, `decisions.yml` and `products.yml`, so
the next report starts from them. `output/` is not checked in; any report can
be rebuilt by setting its period in `pis.yml` and running `build.py`.

## How dates and versions work

- An arXiv preprint and its published version are separate entries, each
  with its own date, so each can be reported in the period it appeared. If
  both fall in the same period, only the published version is reported.
- Preprint dates come from arXiv (first version posted). Published dates come
  from OpenAlex, or from Crossref when OpenAlex gives only a year. Many IEEE
  records give only a year in Crossref too; then the DOI registration date is
  used, which is close to when the paper went online
  (`date_source: crossref registration` in `candidates.yml`).
- Entries with `date_note` in `candidates.yml` have only a year; set the
  right `date:` in `decisions.yml` if they matter.
- A paper counts for an award only if it is dated after that award's start
  date.
