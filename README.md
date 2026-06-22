# Rangan Research Group website

Source for [sdrangan.github.io](https://sdrangan.github.io) — the lab homepage of
Prof. Sundeep Rangan (NYU Tandon / NYU WIRELESS). Built with
[Jekyll](https://jekyllrb.com/) and the
[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, hosted on
GitHub Pages.

## Editing content (no coding required)

Most content lives in plain YAML data files under [`_data/`](_data/). Edit these
directly on GitHub and the site rebuilds automatically.

| To change... | Edit |
|---|---|
| Group members | [`_data/members.yml`](_data/members.yml) |
| Alumni | [`_data/alumni.yml`](_data/alumni.yml) |
| News items | [`_data/news.yml`](_data/news.yml) |
| Courses (Teaching) | [`_data/courses.yml`](_data/courses.yml) |
| Top menu | [`_data/navigation.yml`](_data/navigation.yml) |
| Bio / home page | [`index.md`](index.md) |
| A project page | the matching file in [`_projects/`](_projects/) |
| Publications page | [`_pages/publications.md`](_pages/publications.md) |

### Adding a group member

Add a block to `_data/members.yml` (copy an existing one). To include a photo,
drop a roughly square image in `assets/images/members/` and set
`photo: members/your-name.jpg`. Leave `photo: ""` to use a placeholder.

### Adding a project

Create a new `.md` file in `_projects/` (copy an existing one). The Research page
lists projects automatically, ordered by the `order:` field in the front matter.
Add a thumbnail to `assets/images/projects/` and set `thumbnail:` to show it.

## Local preview

Requires Ruby. From the repository root:

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000>.

## Notes

- Source materials (bio, proposals, original photo) are kept in
  [`material/`](material/) and are not published as pages.
- The two grant PDFs in `material/` are referenced from project pages but not yet
  published; move them into `assets/` and update the links to make them public.
