# run nbdev_export to convert notebooks to modules
# run nbdev_build_lib to convert notebooks to modules

format:
	nbqa black nbs/
	nbqa isort nbs/
	nbqa blacken-docs nbs/ --nbqa-md

export:
	nbdev_export

test:
	# nbdev_test
	nbdev_test --n_workers 4

	# mypy
	nbqa mypy nbs  --ignore-missing-imports


docs:
	nbdev_docs

all: format export test

prepare_dev_env:
	pipenv install --dev
	pre-commit install
	nbdev_install_hooks
	nbdev_install
	nbdev_test --n_workers 4
	nbdev_docs