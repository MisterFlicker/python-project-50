### Hexlet tests and linter status:
[![Actions Status](https://github.com/MisterFlicker/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/MisterFlicker/python-project-50/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/e67979b46b00901c6162/maintainability)](https://codeclimate.com/github/MisterFlicker/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e67979b46b00901c6162/test_coverage)](https://codeclimate.com/github/MisterFlicker/python-project-50/test_coverage) [![CI check](https://github.com/MisterFlicker/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/MisterFlicker/python-project-50/actions/workflows/main.yml)

## Description

About  
A difference calculator is a program that determines the difference between two data structures. Support for different input formats: yaml, json. Report generation in the formats: plain text, stylish и json.

## Installing
git@github.com:MisterFlicker/python-project-50.git

To install use: make install

To build use: make build

To package install use: make package-install

## How to use

Commant to start generate difference:  
poetry run gendiff --format x a b  
where x - format (json, plain or stylsh)  
a and b - path to files with extension

Example  
[![asciicast](https://asciinema.org/a/595888.svg)](https://asciinema.org/a/595888)
