.PHONY: all run clean .venvm lint test coverage

all: run

run: run-dev

run-dev: .venv
	@CRUD_DB_URL=sqlite:///./debug.db \
	 CRUD_HOST=127.0.0.1 \
	 CRUD_PORT=8000 \
	 scripts/devel/entrypoint.sh

run-prod: .venv
	@scripts/prod/entrypoint.sh

migration: .venv
	@CRUD_DB_URL=sqlite:///./debug.db \
	 scripts/devel/migration.sh

wheel:
	@scripts/build/make_wheel.sh

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
