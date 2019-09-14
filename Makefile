SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run flake8 .

.PHONY: unit
unit:
	@echo "unit: not yet"

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --bare --full-report

.PHONY: test
test: lint unit package
