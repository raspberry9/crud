#!/bin/bash
source scripts/settings.sh

MAIN_SCRIPT=crud/main.py

source ${VIRTUALENV_ACTIVATE}; python ${MAIN_SCRIPT}
