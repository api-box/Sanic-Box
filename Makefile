.PHONY: init check format test coverage htmlcov

init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

check:
	isort --recursive --check-only box tests
	black -S -l 79 --check box tests
	pylint box
	mypy box

format:
	isort -rc -y box tests
	black -S -l 79 box tests

test:
	python -m pytest

coverage:
	python -m pytest --cov box --cov-report term

htmlcov:
	python -m pytest --cov box --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html
