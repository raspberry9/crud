#!/bin/bash
source scripts/common.sh

source ${VIRTUALENV_ACTIVATE}
coverage run -m pytest
coverage report -m
