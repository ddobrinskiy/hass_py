# run nbdev_export to convert notebooks to modules
# run nbdev_build_lib to convert notebooks to modules

format:
	black nbs/*.ipynb

export:
	nbdev_export

test:
	nbdev_test --n_workers 4

docs:
	nbdev_docs

prepare_dev_env:
	pipenv install --dev
	pre-commit install
	nbdev_install_hooks
	nbdev_install
	nbdev_test --n_workers 4
	nbdev_docs

all: format export test
