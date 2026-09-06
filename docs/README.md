# Documentation

The documentation sources live in this folder. The rendered site is **not**
committed: it is built by the `Documentation` GitHub workflow on every push and
published to <https://matthiaskoenig.github.io/pymetadata> from `develop`.

The API reference under `api/` and `objects.json` are generated from the
docstrings by `quartodoc` and are gitignored.

## Build locally

Install the quarto extension once:

```bash
quarto add machow/quartodoc
```

Render the site into `../_site`:

```bash
cd docs
quartodoc build
cd ..
quarto render docs
```

## Write with live preview

```bash
cd docs
quartodoc build --watch
quarto preview
```
