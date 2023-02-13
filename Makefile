install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

all:
	poetry build
	poetry publish --dry-run
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 test_task1 tests

test:
	poetry run pytest -s



