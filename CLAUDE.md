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

# tests
pytest                          # all tests
pytest tests/test_omex.py       # single file
pytest tests/test_omex.py::test_entry_from_dict   # single test
tox r -e py3.14                 # single tox env (py3.11-3.14 available)
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
qualifier (`BQB`/`BQM` from `core/miriam.py`) plus a resource given as an
identifiers.org URL (classic or compact), a bioregistry.io URL, a `urn:miriam:*` URN,
a `collection/term` shorthand, or an arbitrary URL, and normalizes it into
`collection` + `term`. Validation checks the term against the identifiers.org
registry pattern (`webservices/registry.py`). `RDFAnnotationData` enriches an
annotation with label/description/synonyms/xrefs by querying OLS.

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
`chebi.py` and `unichem.py`, all going through the shared, retrying session of
`webservices/webservice.py`, whose `get_json` turns an unreachable service, an
error response and a non-JSON body into one `WebserviceError`. They share the
JSON cache helpers in `cache.py`, gated by the module-level globals
`pymetadata.CACHE_USE` (default `True`) and `pymetadata.CACHE_PATH`
(`~/.cache/pymetadata`). These are read at call time, so consumers override them by
assigning `pymetadata.CACHE_PATH = ...` after import. Cached content expires
after `CACHE_DURATION_ONTOLOGY` (30 days, for OLS/ChEBI/UniChem, which describe
an ontology release) or `CACHE_DURATION_REGISTRY` (24 h, for the identifiers.org
registry). When a refresh fails, `read_json_cache_fallback` returns the outdated
content with a warning instead of failing, so queries answered before keep
working offline; `tests/test_offline.py` covers this per service. The corresponding tests
(`test_ols.py`, `test_registry.py`, `test_chebi.py`, `test_unichem.py`) require
network access.

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
- Every module, class and function carries full type annotations and a google-style
  docstring.
- `examples/` at the top level holds the runnable usage examples, they are not
  part of the package: `examples/omex/` collects the COMBINE archive examples
  together with the archives they use (`test.omex`, `biomodels_omex/`). Test
  fixtures live in `tests/data/`.
- Release notes go in `release-notes/` as part of a release commit.
