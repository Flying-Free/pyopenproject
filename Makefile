VENV_NAME=venv
VENV_ACTIVATE=. ./$(VENV_NAME)/Scripts/activate
PYTHON=./${VENV_NAME}/Scripts/python.exe

.DEFAULT_GOAL=help

environment: requirements.txt
	python -m ${VENV_NAME} ./${VENV_NAME} && \
	${VENV_ACTIVATE} && \
	pip install -Ur requirements.txt

test: environment
	- cd ./tests/infra && \
	 docker-compose up -d && printf 'WAITING FOR APIv3' && \
	 until $$(curl --output /dev/null --silent --head --fail http://localhost:8080); do \
	 	printf '.'; \
	 	sleep 5; \
	 done && printf '\n'

	- ${PYTHON} -m unittest discover -s ./tests/test_cases -t tests/test_cases -p *_test.py

	- cd ./tests/infra && \
	  docker-compose down --volumes

help:
	@echo "    clean"
	@echo "        Remove all artifacts."	
	@echo '    build'
	@echo '        Build the project package'
	@echo '    test'
	@echo '        Run tests '

.PHONY: clean help test
