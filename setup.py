#!/usr/bin/env python
from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

requirements = [
    "typing-extensions",
]

setup(
    name="syncio",
    version="v0.0.1",
    description="type safe for synchronous python concurrently",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="guangrei",
    author_email="myawn@pm.me",
    url="https://github.com/guangrei/syncio",
    packages=["syncio"],
    package_data={"syncio": ["py.typed"]},
    license="MIT",
    platforms="any",
    install_requires=requirements,
)
