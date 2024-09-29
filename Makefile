.PHONY: all run clean .venvm lint test

all: run-dev

run-dev: .venv
	@scripts/devel/entrypoint.sh

run-prod: .venv
	@scripts/prod/entrypoint.sh

.venv:
	@scripts/devel/make_venv.sh

lint: .venv
	@scripts/devel/lint.sh

test: .venv
	@scripts/devel/test.sh

clean:
	@rm -rf .venv build dist
	@find . -type f -name '*.py[co]' -delete -o \
		-type d -name __pycache__ -delete
