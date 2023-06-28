install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip uninstall zvonok-test-assignment -y
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8

test:
	poetry run pytest

setup: install build package-install
