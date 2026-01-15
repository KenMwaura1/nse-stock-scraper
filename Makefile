.PHONY: help install test lint

help:
	@echo "Targets: install, test, lint"

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests -p "test_*.py" -v

lint:
	pip install flake8
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
