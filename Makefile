.PHONY: all run clean .venvm lint

all: run-dev

run-dev: .venv
	@scripts/devel/entrypoint.sh

run-prod: .venv
	@scripts/prod/entrypoint.sh

.venv:
	@scripts/devel/make_venv.sh

lint:
	@scripts/devel/lint.sh

clean:
	@rm -rf .venv build dist
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
