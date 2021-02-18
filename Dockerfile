FROM python:3

ENV Version=v0.0.1

RUN apt-get install xz-utils && tar -C /tmp/ -xf /tmp/glib-2.52.1.tar.xz

RUN curl -s https://github.com/Flying-Free/python-openproject-api/archive/${Version}.tar.gz

RUN python -m pip install --user --upgrade setuptools wheel \
python3 setup.py sdist bdist_wheel
