import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openproject-sdk",  # Replace with your own username
    version="0.0.1",
    author="Alan Padierna & Marcelo Torrejon",
    author_email="alanpadierna9595@gmail.com; marcelo.torrejn@gmail.com",
    description="Openproject SDK for Python developers",
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
