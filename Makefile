.PHONY: venv
venv:
	pip install virtualenv && virtualenv venv

.PHONY: run
run:
	pip install -r requeriments.txt
	python3 get_action.py
