SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run flake8 .

.PHONY: unit
unit:
	poetry run sh bin/test.sh

.PHONY: typecheck
typecheck:
	poetry run sh bin/typecheck.sh

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --bare --full-report

.PHONY: test
test: lint typecheck unit package
