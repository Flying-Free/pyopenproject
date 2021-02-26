import os

import setuptools

VERSION = os.getenv('VERSION')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyopenproject",  # Replace with your own username
    version=VERSION,
    author="Alan Padierna Fernández",
    author_email="alanpadierna9595@gmail.com",
    description="Python library to manage OpenProject API endpoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Flying-Free/python-openproject-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
