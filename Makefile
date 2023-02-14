install:
	poetry install

lint:
	poetry run flake8 test_task1 tests

test:
	poetry run pytest -s



