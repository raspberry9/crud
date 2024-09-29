#!/bin/bash
source scripts/devel/settings.sh

CRUD_PORT=${CRUD_PORT:-8000}

source ${VIRTUALENV_ACTIVATE}

export PYTHONDONTWRITEBYTECODE=1

fastapi dev crud/main.py
