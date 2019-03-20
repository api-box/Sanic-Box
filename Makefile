.PHONY: init check test coverage htmlcov

init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

check:
	flake8 rainmq --import-order-style=smarkets --max-complexity 12 max-line-length=79
	black -S -l 79 --check box tests
	mypy box

test:
	make check
	python -m pytest

coverage:
	python -m pytest --cov box --cov-report term

htmlcov:
	python -m pytest --cov box --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html
