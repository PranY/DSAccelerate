.PHONY: download run init

requirements:
	pip3 install -r requirements.txt

run:
	python3 main.py

help:
	cat Makefile

init:
	python __init__.py $(filter-out $@,$(MAKECMDGOALS))

update:
	python update.py $(filter-out $@,$(MAKECMDGOALS))
