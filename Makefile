.PHONY: all run clean .venv

all: run

run: .venv
	@scripts/devel/entrypoint.sh

.venv:
	@scripts/devel/make_venv.sh

clean:
	@rm -rf .venv
