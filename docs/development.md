# Development

Contributions are welcome. The repository is [matthiaskoenig/pymetadata](https://github.com/matthiaskoenig/pymetadata); development happens on the `develop` branch.

## Setup development environment

To set up everything for the development environment use

```bash
# install core dependencies
uv sync

# install dev dependencies
uv pip install -r pyproject.toml --extra dev
uv tool install tox --with tox-uv

# setup pre-commit hook
uv pip install pre-commit
pre-commit install
pre-commit run
```

The pre-commit hooks run the linter, the formatter and the type checker, i.e., the same checks that run in continuous integration.

## Testing

Testing is performed with pytest and tox:

Run single tox target:
```bash
tox r -e py314
```
Run all tests in parallel:
```bash
tox run-parallel
```

To run the tests directly against the current environment use

```bash
pytest                                            # the full suite
pytest tests/test_omex.py                         # a single module
pytest tests/test_omex.py::test_entry_from_dict   # a single test
```

Some tests query web services (identifiers.org, OLS, ChEBI, UniChem) and therefore require network access.

## Linting and formatting

Linting and formatting use [ruff](https://docs.astral.sh/ruff/):

```bash
ruff check     # lint
ruff format    # format
```

## Type checking

Type checking is performed with [ty](https://docs.astral.sh/ty/):

```bash
tox r -e ty
```
Or directly in the working tree:
```bash
uvx ty check
```

The configuration lives in `[tool.ty]` in `pyproject.toml`. Warnings are treated as errors, so the codebase is kept free of diagnostics. Suppress an unavoidable diagnostic with a rule specific `# ty: ignore[rule-name]` rather than a blanket comment.

## Documentation

The documentation is built with [Zensical](https://zensical.org/), the static site generator of the Material for MkDocs authors. The sources are markdown files in `docs/`, the site is configured in `zensical.toml` in the repository root. Nothing rendered is committed: the site is built by the `documentation` workflow on every push and published to [matthiaskoenig.github.io/pymetadata](https://matthiaskoenig.github.io/pymetadata) from the `develop` branch.

Build the site into `site/`:

```bash
uv run zensical build --clean
```

For writing, the preview rebuilds on save:

```bash
uv run zensical serve
```

The API reference is rendered from the docstrings by [mkdocstrings](https://mkdocstrings.github.io/); a page in `docs/api/` only contains the module directive:

```markdown
# omex

::: pymetadata.omex
```

Docstrings are therefore the place to document functions and classes, the markdown files provide the narrative around them. Adding a module to the reference means adding such a page and an entry to `nav` in `zensical.toml`.

### Files for agents { #files-for-agents }

Agents and language models read markdown, not rendered html. `scripts/llms_txt.py` writes the files of the [llms.txt convention](https://llmstxt.org/) into the built site, i.e., [llms.txt](https://matthiaskoenig.github.io/pymetadata/llms.txt) as an annotated index of all pages, [llms-full.txt](https://matthiaskoenig.github.io/pymetadata/llms-full.txt) with the complete documentation in a single file, and the markdown of every page next to its html (`/omex.md` for `/omex/`). The markdown of the API reference is generated from the docstrings with `inspect`, since the pages themselves only contain the mkdocstrings directive.

```bash
uv run zensical build --clean
uv run python scripts/llms_txt.py
```

The `documentation` workflow runs both steps, so the files are regenerated with every push. `docs/robots.txt` points crawlers at the sitemap and at these files. Zensical will provide agent context files itself at some point, then this script can go.

## Regenerating the ontology enums { #regenerating-the-ontology-enums }

`pymetadata.ontologies.sbo`, `kisao`, `eco` and `pbpko` are generated modules and should not be edited by hand. They are rendered from the ontology releases with

```bash
uv sync --extra ontology
python -m pymetadata.ontologies.ontology
```

This needs the optional `ontology` dependencies (`pronto` and `jinja2`), which are not installed with the package because the generated enums work without them. The development environment (`--extra dev`) includes them.

It downloads the OWL files listed in `ontology_files`, stores them gzipped under `src/pymetadata/resources/ontologies/` (not part of the repository), and renders one python module per ontology from `resources/templates/ontology_enum.pytemplate`. Adding an ontology means adding an `OntologyFile` entry and a `create_ontology_enum` call with the id pattern of the ontology.

Run `ruff format` afterwards, since the rendered modules are not formatted.

## Release

A release is made from `develop`:

1. update the ontology enums, see [Regenerating the ontology enums](#regenerating-the-ontology-enums), and commit the changes
2. write the release notes for the version in `release-notes/`
3. make sure everything passes: `tox run-parallel`, `ruff check`, `tox r -e ty`
4. check the version bump: `uvx bump-my-version bump [major|minor|patch] --dry-run -vv`
5. bump the version: `uvx bump-my-version bump [major|minor|patch]`, which updates `src/pymetadata/__init__.py` and `CITATION.cff`, commits and tags
6. `git push --tags`, which triggers the release workflow publishing to [pypi](https://pypi.org/project/pymetadata/), followed by `git push`
7. test the installation from pypi in a fresh environment:

    ```bash
    uv venv --python 3.14
    uv pip install pymetadata
    ```

8. once Zenodo has archived the release, update the citation information: `date-released` in `CITATION.cff` and the version, date and version DOI in the BibTeX of `README.md` and `docs/index.md`
