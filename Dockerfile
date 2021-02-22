FROM python:3

ENV Version="v0.0.1"

# Install dependences
RUN apt-get install --no-install-recommends -y xz-utils=5.2.2 \
    tar -C /tmp/ -xf /tmp/glib-2.52.1.tar.xz \
    python -m pip install --user --upgrade setuptools wheel

# Download the release linked to the version
RUN curl -L -O https://github.com/Flying-Free/python-openproject-api/archive/${Version}.tar.gz \
    tar xvzf ${Version}.tar.gz

# Make the package
RUN python setup.py sdist bdist_wheel

# Upload the package to the repository
