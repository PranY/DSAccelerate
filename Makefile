.PHONY: download run

download:
	pip3 install -r requirements.txt

run:
	python3 main.py

help:
	cat Makefile
