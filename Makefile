VENV_NAME=venv
VENV_ACTIVATE=. ./$(VENV_NAME)/Scripts/activate
PYTHON=./${VENV_NAME}/Scripts/python.exe

.DEFAULT_GOAL=build

pyenv: requirements.txt
	python -m ${VENV_NAME} ./${VENV_NAME} && \
	${VENV_ACTIVATE} && \
    ${PYTHON} -m pip install --upgrade pip && \
	${PYTHON} -m pip install -Ur requirements.txt && \
	${PYTHON} -m pip install coverage


clean_pyenv:
	rm -rf ./${VENV_NAME}

env_reset: clean_pyenv env_down pyenv env_up

env_up:
	cd ./tests/infra && \
	docker-compose up -d && printf '\nWAITING FOR APIv3' && \
	until $$(curl --output /dev/null --silent --head --fail http://localhost:8080); do \
		printf '.'; \
		sleep 5; \
	done && printf '\n\n' && \
	printf '############################\n' && \
	printf '############################\n' && \
	printf '####### UP & RUNNING #######\n' && \
	printf '############################\n' && \
	printf '############################'


pytest:
	- ${PYTHON} -m coverage run -m unittest discover -s ./tests/test_cases -t tests/test_cases -p *_test.py

env_down:
	cd ./tests/infra && \
	docker-compose down --volumes

test: pyenv env_up pytest env_down clean_pyenv

build:
	- python -m pip install --upgrade build
	- python -m build

clean: clean_pyenv
	- rm -rf ./pyopenproject.egg-info ./build ./dist .coverage

vars:
	source ./.env && \
	export VERSION && \
	echo "$$VERSION"


help:
	@echo "    clean"
	@echo "        Remove all artifacts."	
	@echo '    build'
	@echo '        Build the project package'
	@echo '    test'
	@echo '        Run tests '

.PHONY: clean help test build
