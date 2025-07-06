REQUIE = requirements.txt

(NAME): setup

setup:
	pip install -r $(REQUIE)

PHONY: setup