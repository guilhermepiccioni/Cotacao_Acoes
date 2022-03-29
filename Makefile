.PHONY: venv
venv:
	pip install virtualenv && virtualenv venv

.PHONY: run
run:
	pip install -r requeriments.txt
	python3 get_action.py

This project aims to collect data from a specific investment portfolio and generate graphs according to the stipulated date. Made in python with Tkinter and Pandas.
