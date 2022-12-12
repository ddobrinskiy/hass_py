# run nbdev_export to convert notebooks to modules
# run nbdev_build_lib to convert notebooks to modules

format:
	nbqa black nbs/
	nbqa isort nbs/
	nbqa blacken-docs nbs/ --nbqa-md

export:
	nbdev_export


mypy:
	nbqa mypy nbs --ignore-missing-imports

test:
	nbdev_test --n_workers 4

prepare:
	# Export, test, and clean notebooks, and render README if needed
	nbdev_prepare

docs:
	nbdev_docs

generate_deps: Pipfile
	python setup_generate.py

bump: all docs generate_deps
	nbdev_bump_version

all: format prepare mypy

prepare_dev_env:
	pipenv install --dev
	pre-commit install
	nbdev_install_hooks
	nbdev_install
	nbdev_test --n_workers 4
	nbdev_docs