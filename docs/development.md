# Development

Contributions are welcome. The repository is [matthiaskoenig/pymetadata](https://github.com/matthiaskoenig/pymetadata); development happens against the `develop` branch via pull requests.

## Branch model

Two branches are permanent:

- **`develop`** is the default branch and the branch everything is integrated
  into. The documentation on
  [matthiaskoenig.github.io/pymetadata](https://matthiaskoenig.github.io/pymetadata)
  is published from it.
- **`main`** tracks the latest published release. It is fast-forwarded to the
  released commit by the `sync-main` job of the `CI-CD` workflow after the
  package went to pypi, so `main` and the newest version on pypi always agree.
  Nothing is developed on `main` and nothing is merged into it by hand.

Work happens on short lived branches off `develop`, which GitHub deletes after
the merge. Releases are tagged on `develop`, see [Release](#release).

## Pull requests

Neither branch accepts a direct push, every change goes through a pull request
against `develop`. This includes the maintainer, there is no bypass.

A pull request can only be merged once the four required checks are green:

| check   | workflow      | content                                                              |
| ------- | ------------- | -------------------------------------------------------------------- |
| `tests` | `ci-cd.yml`   | the test matrix, linux, macos and windows with python 3.11 to 3.14    |
| `ruff`  | `ruff.yml`    | `ruff check` and `ruff format --check`                                |
| `ty`    | `ty.yml`      | `tox r -e ty`                                                         |
| `docs`  | `docs.yml`    | the zensical build including the api reference and the agent files    |

`tests` aggregates the test matrix into a single job, so the name of the
required check stays the same when the matrix changes.

Further rules of a pull request:

- conversations have to be resolved before the merge
- an approval is dismissed when new commits are pushed
- the history stays linear, i.e., a pull request is merged with squash or
  rebase; merge commits are disabled
- a pull request of a contributor needs a review and the approval of the
  maintainer, who owns the whole repository in `.github/CODEOWNERS`. The
  maintainer merges their own pull requests without an approval, since GitHub
  does not allow approving ones own pull request

[Auto-merge](https://docs.github.com/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request)
is enabled for the repository, so a pull request can be queued and is merged as
soon as the checks pass and the required approval is there.

### Repository policies { #repository-policies }

The protection is implemented with
[repository rulesets](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
They are part of the repository in `.github/rulesets/` instead of only living in
the web interface, so a change to a policy is reviewed like any other change:

| ruleset                 | applies to | rules                                                                                                                                       |
| ----------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `develop.json`          | `develop`  | pull request required, the four checks above, resolved conversations, linear history, no force push, no deletion. **No bypass, for anybody.** |
| `develop-review.json`   | `develop`  | one approving review of a code owner; bypassed by the repository admin                                                                       |
| `main.json`             | `main`     | linear history, no force push, no deletion; bypassed by the GitHub Actions app, which fast-forwards the branch on a release                   |
| `tags.json`             | all tags   | a tag cannot be deleted or moved, so a release tag keeps pointing at what was released                                                       |

Changing a policy means changing the json and applying it:

```bash
.github/rulesets/apply.sh
```

The script is idempotent: it updates the rulesets which exist and creates the
missing ones. It also sets the merge settings of the repository, i.e.,
auto-merge, delete branch on merge, and squash and rebase as the only merge
methods. It needs the [github cli](https://cli.github.com) authenticated as a
user with admin permission on the repository.

## Setup development environment

Development needs [uv](https://docs.astral.sh/uv/) and a checkout of the repository:

```bash
git clone https://github.com/matthiaskoenig/pymetadata.git
cd pymetadata
```

A single sync creates the virtual environment in `.venv`, installs `pymetadata` into it in editable mode and adds the complete tooling:

```bash
uv sync --extra dev
```

The `dev` extra contains everything used below, i.e., pytest, ruff, ty, tox, pre-commit, zensical and bump-my-version, and it pulls in the optional `ontology` extra, so nothing has to be installed separately. The python version is taken from `.python-version` (currently 3.14); to work against the oldest supported version instead use `uv sync --extra dev --python 3.11`, which replaces the environment.

The tools are then run either with `uv run <command>`, which uses the environment without activating it, or from the activated environment:

```bash
source .venv/bin/activate        # Linux and macOS
.venv\Scripts\activate           # Windows
```

The commands in this document are written without the `uv run` prefix; prepend it if the environment is not activated.

The last step installs the git hook:

```bash
uv run pre-commit install          # install the hook, once per checkout
uv run pre-commit run --all-files  # check the current state of the repository
```

From now on every commit is checked with ruff (lint and format) and ty, i.e., the same checks that run in continuous integration. On a commit only the changed files are looked at, `--all-files` checks the whole repository and is what a newly added hook should be tried with.

## Testing

The tests are written with pytest, tox runs them against every supported python version.

The tox environments are named after the interpreter (`py3.11` to `py3.14`, see `envlist` in `tox.ini`), a single one is run with
```bash
tox r -e py3.14
```
and the complete matrix, including the `ty` environment, in parallel with
```bash
tox run-parallel
```

This needs the interpreters to be available, which uv installs with `uv python install 3.11 3.12 3.13 3.14`. Continuous integration runs the same environments as `uvx --with tox-uv tox -e py3.14`.

To run the tests directly against the development environment use

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

## Regenerating the ontologies { #regenerating-the-ontologies }

`pymetadata.ontologies.sbo`, `kisao` and `pbpko` are generated modules and should not be edited by hand. They are rendered from the ontology releases by `pymetadata.ontologies._ontology_builder`, which is internal tooling for maintainers rather than part of the public API, and therefore not in the API reference:

```bash
python -m pymetadata.ontologies._ontology_builder
```

This needs the optional `ontology` dependency (`pronto`), which is not installed with the package because the generated terms work without it. It is part of the development environment, so `uv sync --extra dev` covers it.

It downloads the OWL files of the packaged ontologies, stores them gzipped under `src/pymetadata/resources/ontologies/` (not part of the repository), and writes one python module per ontology: a class with one attribute per term, documented with the definition of the term so that editors show it, plus the information registered on the class; the behaviour comes from `OntologyTerm` in `pymetadata.ontologies.term`. The modules are written with plain python string building, there is no template engine. Adding an ontology means adding an `OntologyFile` entry and an entry to `ontology_patterns` with the id pattern of the ontology.

Run `ruff format` afterwards, since the rendered modules are not formatted.

## Release

A release is made from `develop`. Since `develop` only accepts pull requests,
the release is prepared on a branch and tagged once that pull request is merged:

1. branch off `develop`: `git switch -c release/x.y.z develop`
2. update the ontology modules, see [Regenerating the ontologies](#regenerating-the-ontologies), and commit the changes
3. write the release notes for the version in `release-notes/x.y.z.md`
4. make sure everything passes: `tox run-parallel`, `ruff check`, `tox r -e ty`
5. check the version bump: `uvx bump-my-version bump [major|minor|patch] --dry-run -vv`
6. bump the version: `uvx bump-my-version bump [major|minor|patch]`, which updates `src/pymetadata/__init__.py` and `CITATION.cff` and commits. It does not create the tag; a squash or rebase merge would rewrite the commit and leave the tag behind on a commit which is not part of `develop`
7. push the branch, open the pull request against `develop` and merge it once the checks are green
8. tag the merged commit on `develop` and push the tag:

    ```bash
    git switch develop
    git pull
    git tag x.y.z
    git push origin x.y.z
    ```

    This starts the `CI-CD` workflow, which runs the test matrix, publishes to
    [pypi](https://pypi.org/project/pymetadata/), creates the GitHub release
    from `release-notes/x.y.z.md` and fast-forwards `main` to the tagged commit.
    Check the version before pushing, a tag cannot be moved or deleted
    afterwards.

9. test the installation from pypi in a fresh environment:

    ```bash
    uv venv --python 3.14
    uv pip install pymetadata
    ```

10. once Zenodo has archived the release, update the citation information, i.e., `date-released` in `CITATION.cff` and the version, date and version DOI of the release in the citation of `README.md` and `docs/index.md`. `bump-my-version` only updates the version, not the date and the DOI, which are only known after the release. These changes go in through a pull request like everything else
