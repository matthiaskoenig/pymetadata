# CLAUDE.md

This file provides guidance when working with code in this repository.

## Project

`pymetadata` is a python library for metadata in the context of COMBINE standards:
COMBINE archives (OMEX), MIRIAM/RDF annotations, and ontology terms (SBO, KISAO, PBPKO).
Pure library, no CLI entry points. Requires python >= 3.11, packaged with hatchling
(version is read from `src/pymetadata/__init__.py`). Runtime dependencies are
`rich`, `requests` and `pydantic`; `pronto` is the optional `ontology` extra,
needed only to regenerate the ontology modules.

## Commands

```bash
# environment (uv based); the dev extra includes the ontology extra
uv sync --extra dev
uv run pre-commit install
uv lock                         # after every change of a dependency in pyproject.toml

# tests
pytest                          # all tests
pytest tests/test_omex.py       # single file
pytest tests/test_omex.py::test_entry_from_dict   # single test
tox r -e py3.15                 # single tox env (py3.11-3.15 available)
tox run-parallel                # full matrix + ty, run before opening a pull request

# lint / format / types
ruff check
ruff format
tox -e ty                       # ty type check (config in [tool.ty] in pyproject.toml)
uvx ty check                    # same check, straight from the working tree
```

`develop` is the default branch and takes every change through a pull request; direct pushes are rejected by the rulesets in `.github/rulesets/` (applied with `.github/rulesets/apply.sh`), which require the `tests`, `ruff`, `ty` and `docs` checks. Continuous integration is kept minimal: `tests` runs only `py3.14`, on linux, macos and windows, every workflow cancels a superseded run (`cancel-in-progress: true`), uv caches packages and interpreters, dependabot runs monthly. The other python versions run only locally. `main` only tracks the latest release and is fast-forwarded by the `sync-main` job of the release workflow, never by hand.

Release steps are in `docs/development.md` (there is no separate `RELEASE.md`):
the release is prepared on a branch, `uvx bump-my-version bump [major|minor|patch]`
updates `src/pymetadata/__init__.py` and `CITATION.cff` and commits without
tagging (`tag = false`, a squash merge would rewrite the commit), and the tag is
created on `develop` after the pull request was merged, which triggers the PyPI
release workflow.

Documentation is [Zensical](https://zensical.org/): markdown sources in `docs/`,
configured in `zensical.toml`, built into the gitignored `site/`
(`uv run zensical build --clean`, `uv run zensical serve` for the preview). The
API reference is rendered from the docstrings by mkdocstrings; a page in
`docs/api/` is just `::: pymetadata.<module>`, so nothing is generated into the
repository. `scripts/llms_txt.py` runs after the build and writes the agent
facing files (`llms.txt`, `llms-full.txt` and the markdown of every page) into
`site/`. The `documentation` workflow runs both and publishes the site from
`develop`.

## Architecture

**`omex.py` — COMBINE archive.** The main module. `Omex` holds a temporary directory
plus a `Manifest` of `ManifestEntry` pydantic models; archives are created/read via
`Omex.from_omex`, `from_url`, `from_directory` and written via `to_omex`,
`to_directory`. `EntryFormat` is a large enum mapping formats to
`http://identifiers.org/combine.specifications/*` or `https://purl.org/NET/mediatypes/*`
URIs; `guess_format`/`lookup_format` resolve a file suffix to such a URI. Manifest
locations are normalized to `./`-prefixed relative paths. `oven/omex_v2.py` is only a
draft pydantic sketch of the COMBINE archive v2 metadata, not wired into `omex.py`;
`oven/` holds unfinished work which is deliberately undocumented and untested.

**`core/annotation.py` — RDF/MIRIAM annotations.** `RDFAnnotation` parses a
qualifier (`BQB`/`BQM` from `core/miriam.py`) plus a resource given as an
identifiers.org URL (classic or compact), a bioregistry.io URL, a `urn:miriam:*` URN,
a `collection/term` shorthand, or an arbitrary URL, and normalizes it into
`collection` + `term`. Validation checks the term against the identifiers.org
registry pattern (`webservices/registry.py`). `RDFAnnotationData` enriches an
annotation with label/description/synonyms/xrefs by querying OLS, and with the
providers of the collection: `url` is the url of the primary provider (the official
non deprecated one, see `primary_resource`), `providers` lists the others, and
`collection_name`, `collection_homepage` and `pattern_match` describe the collection.

**Ontologies are generated code.** `ontologies/sbo.py`, `kisao.py`, `pbpko.py`
are machine-generated (large; do not hand-edit). Each is a class of
`OntologyTerm` attributes (`ontologies/term.py`), not an enum: a term is a `str`
subclass carrying `label`, `definition`, `synonyms`, `deprecated`, `curie` and
`url`, and every term is declared twice, under its id and under its name, with
its definition as attribute docstring so editors show it on completion. The
class body only declares the attributes, `OntologyTerm._register` creates the
terms and sets them. `OntologyMeta` provides the enum-like `len()`, iteration,
`in`, `SBO["SBO_0000247"]` and `SBO("SBO:0000247")`; `get_name()`, `get_term()`
and `validate()` accept both `SBO_0000247` and `SBO:0000247` spellings.
Generation comes from `ontologies/_ontology_builder.py` (internal, not part of
the public API; its `pronto` import is lazy, it is the optional `ontology`
extra): `update_ontology_files()` downloads OWL sources into
`src/pymetadata/resources/ontologies/*.owl.gz` (gitignored, so they must be
re-downloaded before regeneration), `Ontology` reads them with pronto, and
`create_ontology_module(id, pattern)` writes the module into `ONTOLOGY_DIR`,
i.e., `ontologies/<id>.py` (plain python string building, no template engine).
The definition of a term comes from the definition, the comment or the
annotations, since SBO uses `rdfs:comment` and KISAO `skos:definition`. Running
`python -m pymetadata.ontologies._ontology_builder` performs download +
regeneration + import check, and needs `pronto` (part of `--extra dev`).
`ontologies/__init__.py` re-exports `SBO`, `KISAO`, `PBPKO` and their
`<ONTOLOGY>Type` aliases through a module `__getattr__`, so the generated code
is only imported when a term is used and `pymetadata.webservices.ols` stays
cheap (the `pymetadata.metadata` package was removed in 0.6.0).

**Web services + caching.** The `webservices/` package holds everything which
hits a remote API: `ols.py` (EBI OLS4), `registry.py` (identifiers.org),
`chebi.py` (also the svg structure of a compound), `uniprot.py` and `unichem.py`, all going through the shared, retrying session of
`webservices/webservice.py`, whose `get_json` turns an unreachable service, an
error response and a non-JSON body into one `WebserviceError`; a 404 raises its
subclass `WebserviceNotFoundError`, which callers treat as an unknown entry and
never answer from an outdated cache. `get_bytes` does the same for svg images. They share the
JSON cache helpers in `cache.py`, gated by the module-level globals
`pymetadata.CACHE_USE` (default `True`) and `pymetadata.CACHE_PATH`
(`~/.cache/pymetadata`). These are read at call time, so consumers override them by
assigning `pymetadata.CACHE_PATH = ...` after import. Cached content expires
after `CACHE_DURATION_ONTOLOGY` (30 days, for OLS/ChEBI/UniChem, which describe
an ontology release) or `CACHE_DURATION_REGISTRY` (24 h, for the identifiers.org
registry). When a refresh fails, `read_json_cache_fallback` returns the outdated
content with a warning instead of failing, so queries answered before keep
working offline; `tests/test_offline.py` covers this per service. The corresponding tests
(`test_ols.py`, `test_registry.py`, `test_chebi.py`, `test_unichem.py`, `test_uniprot.py`) require
network access. Processes share the cache (pytest-xdist workers): `write_bytes_cache`
and `write_json_cache` write a temporary file next to the cache file and `os.replace`
it, so a reader never sees a partial file, and the write is best effort, a failure is
a warning and the caller keeps its data. On Windows a file another process has open
cannot be replaced and a file being replaced cannot be opened, so both are retried
(`CACHE_IN_USE_ATTEMPTS`); `Registry` uses the downloaded namespaces and does not read
them back. `test_registry.py` loads the registry from several processes into one empty
cache, with the download answered from `tests/data/registry/` (#102).

`console.py` (rich console, for scripts and `__main__` blocks) and `log.py`
provide the shared output/logging. Modules get their logger from the standard
library with `logging.getLogger(__name__)`. The package never configures
logging: no handlers, no levels, only a `NullHandler` on the `pymetadata`
logger; `log.enable_rich_logging()` is the opt-in for scripts. Library code logs, it does not print, and log calls use
lazy `%s` formatting rather than f-strings (enforced by ruff `G`).

## Conventions

- Type checking is done with [ty](https://docs.astral.sh/ty/) (mypy was removed in #69).
  `[tool.ty.terminal] error-on-warning = true` means warnings fail the check, so the tree
  must stay at zero diagnostics; the checked python version is inferred from
  `project.requires-python`. Suppress a diagnostic with a rule-specific
  `# ty: ignore[rule-name]`, never a blanket `# type: ignore`. ty also runs as a
  pre-commit hook (`--extra dev`, so the hook syncs the dev environment it checks against).
- `uv.lock` is committed and pins the local development environment (`uv sync`,
  `uv run`, so also `uv run ty check`), the `documentation` workflow, which runs
  `uv sync --locked`, and the ruff version of the `ruff` workflow; the tox
  environments, i.e. the test matrix and the `ty` check of continuous
  integration, resolve from `pyproject.toml` and do not use it. After changing a
  dependency in `pyproject.toml` run `uv lock`, otherwise the `documentation`
  workflow fails; `uv lock --upgrade` moves the lock to the newest releases.
  Dependabot bumps the lock monthly with `versioning-strategy: lockfile-only`, so
  the lower bounds in `pyproject.toml`, which users install against, are only
  changed by hand.
- Every module, class and function carries full type annotations and a google-style
  docstring.
- `examples/` at the top level holds the runnable usage examples, they are not
  part of the package: `examples/omex/` collects the COMBINE archive examples
  together with the archives they use (`test.omex`, `biomodels_omex/`). Test
  fixtures live in `tests/data/`.
- Release notes go in `release-notes/` as part of a release commit.
