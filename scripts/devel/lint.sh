#!/bin/bash
source scripts/common.sh

source ${VIRTUALENV_ACTIVATE}
pylint crud/**/*.py
