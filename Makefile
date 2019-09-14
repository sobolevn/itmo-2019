SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run flake8 .

.PHONY: unit
unit:
	pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --bare --full-report

.PHONY: test
test: lint unit package
