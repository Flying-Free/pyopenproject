VENV_NAME=venv
VENV_ACTIVATE=. ./$(VENV_NAME)/Scripts/activate
PYTHON=./${VENV_NAME}/Scripts/python.exe

.DEFAULT_GOAL=build

environment: requirements.txt
	python -m ${VENV_NAME} ./${VENV_NAME} && \
	${VENV_ACTIVATE} && \
	pip install -Ur requirements.txt

env_reset: env_down env_up

env_up:
	cd ./tests/infra && \
	docker-compose up -d && printf 'WAITING FOR APIv3' && \
	until $$(curl --output /dev/null --silent --head --fail http://localhost:8080); do \
		printf '.'; \
		sleep 5; \
	done && printf '\n'


pytest:
	${PYTHON} -m unittest discover -s ./tests/test_cases -t tests/test_cases -p *_test.py

env_down:
	cd ./tests/infra && \
	docker-compose down --volumes

test: environment env_up pytest env_down

build: test
	docker build .


help:
	@echo "    clean"
	@echo "        Remove all artifacts."	
	@echo '    build'
	@echo '        Build the project package'
	@echo '    test'
	@echo '        Run tests '

.PHONY: clean help test test
