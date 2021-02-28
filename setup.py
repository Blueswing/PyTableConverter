#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("docs/README.rst") as readme_file:
    readme = readme_file.read()

with open("docs/HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "antlr4-python3-runtime==4.8"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=6",
]

setup(
    author="Yeefea",
    author_email="yifei.shen@yahoo.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Tools for converting tables in different formats.",
    entry_points={
        "console_scripts": [
            "tableconverter=tableconverter.main:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="tableconverter antlr",
    name="tableconverter",
    packages=find_packages(include=["tableconverter", "tableconverter.*"]),
    package_data={"tableconverter": ["util/html_entity.json"]},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Blueswing/tableconverter",
    version="0.1.4",
    zip_safe=False,
)
