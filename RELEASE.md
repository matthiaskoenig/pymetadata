# Release information

## make release
* update ontologies via `ontology.update_ontology_files()`
* update release notes in `release-notes` with commit
* make sure all tests run (`tox run-parallel`)
* check formating and linting (`ruff check`)
* bump version (`bump-my-version bump [major|minor|patch] --dry-run -vv`)



* `git push --tags` (triggers release)
* `git push`

* test installation in virtualenv from pypi
```
mkvirtualenv test --python=python3.13
(test) pip install pymetadata
```

## setup environment

https://github.com/tox-dev/tox-uv
uv tool install tox --with tox-uv
tox r -e py312
tox run-parallel


# install dev dependencies:
```bash
# install dependencies
uv sync
# install dev dependencies
uv pip install -r pyproject.toml --extra dev
# install tox-uv support
uv tool install tox --with tox-uv
```

# pre-commit
pip install pre-commit
pre-commit install

pre-commit run


