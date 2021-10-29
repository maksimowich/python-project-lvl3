reinstall-local:
	poetry run python3 -m pip install --force-reinstall dist/*.whl

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

install:
	poetry install

lint:
	poetry run flake8 page_loader