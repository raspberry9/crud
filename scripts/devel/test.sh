#!/bin/bash
source scripts/common.sh
source ${VIRTUALENV_ACTIVATE}

export PYTHONDONTWRITEBYTECODE=1

pytest -p no:cacheprovider
