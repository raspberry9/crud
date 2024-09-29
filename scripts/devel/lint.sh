#!/bin/bash
source scripts/devel/settings.sh

source ${VIRTUALENV_ACTIVATE}
pylint crud/**/*.py
