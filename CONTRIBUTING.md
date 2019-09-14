# How to contribute

## Tutorials

- Learn how [Github Actions](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/) work
- Learn what [`poetry`](https://github.com/sdispater/poetry) is
- Learn what [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide) is


## Dependencies

We use [poetry](https://github.com/sdispater/poetry) to manage the dependencies.

To install them you would need to run `install` command:

```bash
poetry install
```

To activate your `virtualenv` run `poetry shell`.
You can also prefix your regular commands with `poetry run` like so:

```bash
poetry run which python
```

## Tests

We use `pytest` and `flake8` for quality control.
We also use `wemake_python_styleguide` itself
to develop `wemake_python_styleguide`.

To run all tests:

```bash
pytest
```

To run linting:

```bash
flake8 .
```

These steps are mandatory during the CI.


## Type checks

We use `mypy` to run type checks on our code.
To use it:

```bash
mypy wemake_python_styleguide
```

This step is mandatory during the CI.


## Submitting your code

We use [trunk based](https://trunkbaseddevelopment.com/)
development (we also sometimes call it `wemake-git-flow`).

What the point of this method?

1. We use protected `master` branch,
   so the only way to push your code is via pull request
2. We use issue branches: to implement a new feature or to fix a bug
   create a new branch named `issue-$TASKNUMBER`
3. Then create a pull request to `master` branch

So, this way we achieve an easy and scalable development process
which frees us from merging hell and long-living branches.

In this method, the latest version of the app is always in the `master` branch.

### Before submitting

Before submitting your code please do the following steps:

1. Run `pytest` to make sure everything was working before
2. Add any changes you want
3. Add tests for the new changes
4. Add an integration test into `tests/fixtures/noqa.py`
5. Edit documentation if you have changed something significant
6. Run `pytest` again to make sure it is still working
7. Run `mypy` to ensure that types are correct
8. Run `flake8` to ensure that style is correct

You can run everything at once with `make test`,
see our `Makefile` for more details.
