.PHONY: all run clean .venvm lint test coverage

all: run

run: run-dev

run-dev: .venv
	@CRUD_DB_URL=sqlite:///./debug.db \
	 scripts/devel/entrypoint.sh

run-prod: .venv
	@scripts/prod/entrypoint.sh

migration: .venv
	@CRUD_DB_URL=sqlite:///./debug.db \
	 scripts/devel/migration.sh

.venv:
	@scripts/devel/make_venv.sh

lint: .venv
	@scripts/devel/lint.sh

test: .venv
	@scripts/devel/test.sh

coverage: .venv
	@scripts/devel/coverage.sh

clean:
	@rm -rf .venv build dist
	@find . -type f -name '*.py[co]' -delete -o \
	 -type d -name __pycache__ -delete
	@rm -f debug.db
