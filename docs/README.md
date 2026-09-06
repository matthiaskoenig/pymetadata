# Documentation

The documentation sources live in this folder. The rendered site is **not**
committed: it is built by the `Documentation` GitHub workflow on every push and
published to <https://matthiaskoenig.github.io/pymetadata> from `develop`.

The documentation is built with [Zensical](https://zensical.org/), configured in
`zensical.toml` in the repository root. The API reference under `api/` is
rendered from the docstrings by
[mkdocstrings](https://mkdocstrings.github.io/), the pages only contain the
`::: pymetadata.<module>` directive.

## Build locally

```bash
uv run zensical build --clean   # into ../site
```

## Write with live preview

```bash
uv run zensical serve
```
