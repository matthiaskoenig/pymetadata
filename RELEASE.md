# Release information

## make release
* update ontologies via `ontology.update_ontology_files()`
* update release notes in `release-notes` with commit
* make sure all tests run (`tox -p`)
* bump version (`bumpversion [major|minor|patch]`)
* `git push --tags` (triggers release)
* `git push`

* test installation in virtualenv from pypi
```
mkvirtualenv test --python=python3.11
(test) pip install pymetadata
```

## setup environment
https://github.com/tox-dev/tox-uv
uv tool install tox --with tox-uv
tox r -e py312
tox run-parallel


# install dev dependencies:
uv pip install -r pyproject.toml --extra dev



