# run nbdev_export to convert notebooks to modules
# run nbdev_build_lib to convert notebooks to modules

format:
	black nbs/*.ipynb

export:
	nbdev_export

test:
	nbdev_test --n_workers 4

all: format export test
