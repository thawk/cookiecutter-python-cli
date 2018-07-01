# If the first argument is "run"...
ifeq (run,$(firstword $(MAKECMDGOALS)))
	# use the rest as arguments for "run"
	RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
endif

%:
	@:

init:
	pip install pipenv
	pipenv install --dev

PHONY: test
test:
	py.test tests

PHONY: run
run:
	pipenv run python -m {{cookiecutter.app_name}} $(RUN_ARGS)

