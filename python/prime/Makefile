POETRUN:= poetry run
PYDIR:= src tests

coverage-report:
	$(POETRUN) coverage html -d .coverage_cache
	open .coverage_cache/index.html

check:
check: format-check lint mypy test

format:
	$(POETRUN) black $(PYDIR)

format-check:
	$(POETRUN) black --check $(PYDIR)

lint:
	$(POETRUN) ruff check $(PYDIR) $(args)

mypy:
	$(POETRUN) mypy $(PYDIR)

run:
	$(POETRUN) python src/app.py $(args)

setup:
	echo "Installing Poetry"
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install

define run_tests
	$(POETRUN) coverage run --source src -m pytest $(1)
	$(POETRUN) coverage report
endef

.PHONY: test
test:
	$(call run_tests, $(args))

clean:
	echo "Uninstalling Poetry"
	curl -sSL https://install.python-poetry.org | python3 - --uninstall
