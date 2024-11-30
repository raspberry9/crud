#!/bin/bash
source scripts/common.sh

source ${VIRTUALENV_ACTIVATE}

check_requirements coverage pytest

coverage run -m pytest
coverage report -m
