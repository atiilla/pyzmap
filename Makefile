.PHONY: install format lint clean

install:
	poetry install
	pre-commit install

format:
	poetry run isort pyzmap
	poetry run black pyzmap

lint:
	poetry run isort --check-only --diff .
	poetry run black --check .
	poetry run pyupgrade --py311-plus $$(find . -name '*.py' -not -path './.venv/*')

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
pytest:
	poetry run pytest