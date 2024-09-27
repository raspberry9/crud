#!/bin/bash
source scripts/settings.sh
source ${VIRTUALENV_ACTIVATE}
pylint crud/**/*.py
