Pip ?= pip
Python ?= python

export_req:
	$(Pip) freeze > requirements.txt

dev:
	$(Pip) install -e .

release:
	$(Python) setup.py check
	$(Python) setup.py sdist
