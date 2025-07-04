[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![codecov](https://codecov.io/gh/fcbg-platforms/meg-wiki/graph/badge.svg?token=XxO34oZis3)](https://codecov.io/gh/fcbg-platforms/meg-wiki)
[![tests](https://github.com/fcbg-platforms/meg-wiki/actions/workflows/pytest.yaml/badge.svg?branch=main)](https://github.com/fcbg-platforms/meg-wiki/actions/workflows/pytest.yaml)
[![doc](https://github.com/fcbg-platforms/meg-wiki/actions/workflows/doc.yml/badge.svg?branch=main)](https://github.com/fcbg-platforms/meg-wiki/actions/workflows/doc.yml)

# MEG wiki

The MEG-wiki is available at the address: https://meg-wiki.fcbg.ch
Contributions in all forms are welcome. Please use the
[issue tracker](https://github.com/fcbg-platforms/meg-wiki/issues) to propose changes,
additions and report issues and solutions found when working with MEG data from our
site.

# Contribution

## Pull request and structure

Pull request to the repository are welcome. The wiki is organized as a python project
with a sphinx documentation. The documentation, used to generate the website HTML pages,
is written in reStructuredText format in the
[doc](https://github.com/fcbg-platforms/meg-wiki/tree/main/doc) folder.

In a pull request, the automatic workflows will build the documentation and check for
conformity. Any warnings and errors during the build process must be resolved before the
pull request can be merged.

## Building the documentation locally

After cloning the repository, the project and its dependencies can be installed in a
python environment with:

```
$ pip install -e path/to/meg-wiki[all]
```

Additionally, pre-commit hooks are available to check for common errors before
committing changes.

```
$ pip install pre-commit
$ pre-commit install
```

The documentation can be build from the `meg-wiki/doc` folder with `make` commands:

- `make html` to build the entire website.
- `make html-noplot` to build the website without running the tutorials.
- `make clean` to remove the generated and build files.
- `make view` to open the build website in the default browser.
- `make linkcheck` followed by `make linkcheck-grep` to test for broken URLs.

## Additional information

Additional information can be found on the
[contributing guide](https://meg-wiki.fcbg.ch/contributing.html).


## Updating registry

Whenever a change is made to the [meg-wiki-datasets](https://github.com/fcbg-platforms/meg-wiki-datasets),  the `sample-registry.txt` must be updated accordingly:

```python
from meg_wiki.datasets.sample import _make_registry 
_make_registry(r"PATH_TO_meg-wiki-datasets")
```

