.PHONY: all run clean .venv

all: run

run: .venv
	@scripts/devel/entrypoint.sh

.venv:
	@scripts/devel/make_venv.sh

lint:
	@scripts/devel/lint.sh

clean:
	@rm -rf .venv
