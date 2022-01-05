#!/bin/bash
# pipenv and jupyter must be installed

pipenv install
jupyter execute iris-flowers-classification-ml-project.ipynb
pipenv run test
