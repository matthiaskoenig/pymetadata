# CLAUDE.md

This file provides guidance when working with code in this repository.

## Project

`pymetadata` is a python library for metadata in the context of COMBINE standards:
COMBINE archives (OMEX), MIRIAM/RDF annotations, and ontology enums (SBO, KISAO, ECO, PBPKO).
Pure library, no CLI entry points. Requires python >= 3.11, packaged with hatchling
(version is read from `src/pymetadata/__init__.py`). Runtime dependencies are
`rich`, `requests` and `pydantic`; `pronto` and `jinja2` are the optional
`ontology` extra, needed only to regenerate the enums.

## Commands

```bash
# environment (uv based)
uv sync
uv pip install -r pyproject.toml --extra dev
uv tool install tox --with tox-uv
pre-commit install

# tests
pytest                          # all tests
pytest tests/test_omex.py       # single file
pytest tests/test_omex.py::test_entry_from_dict   # single test
tox r -e py314                  # single tox env (py3.11-3.14 available)
tox run-parallel                # full matrix + ty

# lint / format / types
ruff check
ruff format
tox -e ty                       # ty type check (config in [tool.ty] in pyproject.toml)
uvx ty check                    # same check, straight from the working tree
```

Release steps are in `docs/development.md` (there is no separate `RELEASE.md`);
version bumps go through `uvx bump-my-version bump [major|minor|patch]` (updates
`src/pymetadata/__init__.py` and `CITATION.cff`), and pushing the tag triggers
the PyPI release workflow.

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
qualifier (`BQB`/`BQM` from `identifiers/miriam.py`) plus a resource given as an
identifiers.org URL (classic or compact), a bioregistry.io URL, a `urn:miriam:*` URN,
a `collection/term` shorthand, or an arbitrary URL, and normalizes it into
`collection` + `term`. Validation checks the term against the identifiers.org
registry pattern (`identifiers/registry.py`). `RDFAnnotationData` enriches an
annotation with label/description/synonyms/xrefs by querying OLS.

**Ontology enums are generated code.** `ontologies/sbo.py`, `kisao.py`,
`eco.py`, `pbpko.py` are machine-generated (large; do not hand-edit). They come
from `ontologies/ontology.py` (whose `pronto`/`jinja2` imports are lazy, they are
the optional `ontology` extra): `update_ontology_files()` downloads OWL sources
into `src/pymetadata/resources/ontologies/*.owl.gz` (gitignored, so they must be
re-downloaded before regeneration), `Ontology` reads them with pronto, and
`create_ontology_enum(id, pattern)` renders
`resources/templates/ontology_enum.pytemplate` into `ENUM_DIR`, i.e.,
`ontologies/<id>.py`. Running `python -m pymetadata.ontologies.ontology`
performs download + regeneration + import check, and needs
`uv sync --extra ontology`. Each generated enum exposes `get_name()` and
`validate()` accepting both `SBO_0000247` and `SBO:0000247` spellings; ids are
stored with underscores. `ontologies/__init__.py` re-exports `SBO`, `KISAO`,
`ECO`, `PBPKO` and their `<ONTOLOGY>Type` aliases through a module `__getattr__`,
so the ~1 MB of generated code is only imported when a term is used and
`pymetadata.ontologies.ols` stays cheap (the `pymetadata.metadata` package was
removed in 0.6.0).

**Web services + caching.** `ontologies/ols.py` (EBI OLS4), `identifiers/registry.py`
(identifiers.org), `chebi.py`, `unichem.py` all hit remote APIs and share the JSON
cache helpers in `cache.py`, gated by the module-level globals
`pymetadata.CACHE_USE` (default `False`) and `pymetadata.CACHE_PATH`
(`~/.cache/pymetadata`). These are read at call time, so consumers override them by
assigning `pymetadata.CACHE_PATH = ...` after import. The corresponding tests
(`test_ols.py`, `test_registry.py`, `test_chebi.py`, `test_unichem.py`) require
network access.

`console.py` (rich console, for scripts and `__main__` blocks) and `log.py`
(`log.get_logger(__name__)`, a plain `logging.getLogger`) provide the shared
output/logging. The package never configures logging: no handlers, no levels,
only a `NullHandler` on the `pymetadata` logger; `log.enable_rich_logging()` is
the opt-in for scripts. Library code logs, it does not print, and log calls use
lazy `%s` formatting rather than f-strings (enforced by ruff `G`).

## Conventions

- Type checking is done with [ty](https://docs.astral.sh/ty/) (mypy was removed in #69).
  `[tool.ty.terminal] error-on-warning = true` means warnings fail the check, so the tree
  must stay at zero diagnostics; the checked python version is inferred from
  `project.requires-python`. Suppress a diagnostic with a rule-specific
  `# ty: ignore[rule-name]`, never a blanket `# type: ignore`. ty also runs as a
  pre-commit hook (`--extra dev`, so the hook syncs the dev environment it checks against).
- Every module, class and function carries full type annotations and a google-style
  docstring.
- `src/pymetadata/examples/` holds runnable usage examples plus test data
  (`test.omex`, `biomodels_omex_example/`); test fixtures live in `tests/data/`.
- Release notes go in `release-notes/` as part of a release commit.
