.PHONY: download run

download:
	pip3 install --user -r requirements.txt

run:
	python3 main.py