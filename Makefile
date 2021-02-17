VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)\Scripts\activate
PYTHON=${VENV_NAME}\Scripts\python

.DEFAULT_GOAL=help

environment: requirements.txt
	
	python -m venv .\venv

	.\venv\Scripts\activate && \
	pip install -U setuptools \
	pypiwin32 \
	pywin32 && \
	pip install -Ur requirements.txt

compile: clean environment
	
clean: clean-pyc clean-build
	- if exist ".idea\" rmdir /q /s .idea
	- if exist "venv" rmdir /Q /S venv

clean-pyc:
	- del /s /q *.pyc
	- del /s /q *.pyo
	- powershell.exe "get-childitem -Include __pycache__ -Recurse -force | Remove-Item -Force -Recurse"

clean-build:
	- if exist "build" rmdir /s /q "build"
	- if exist "dist" rmdir /s / q "dist"
	- del *.egg-info
	- del *.spec

test:
	- .\venv\Scripts\python.exe ./tests/infra/reset_infra.py
	- .\venv\Scripts\python.exe -m unittest discover -s ./tests/test_cases -t tests\test_cases -p *_test.py

delivery: clean environment
    #pip install of test required dependencies
    - pip install -U
    #Generate lib
help:
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo "    clean-build"
	@echo "        Remove build artifacts."
	@echo "    clean"
	@echo "        Remove all artifacts."	
	@echo '    compile'
	@echo '        Compile the project to perform a new setup'
	@echo '    venv'
	@echo '        Build the project virtual environment using python environments'
	@echo '    test'
	@echo '        Run tests '

.PHONY: clean venv help compile
