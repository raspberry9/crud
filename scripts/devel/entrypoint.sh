#!/bin/bash
source scripts/common.sh

CRUD_PORT=${CRUD_PORT:-8000}

source ${VIRTUALENV_ACTIVATE}

export PYTHONDONTWRITEBYTECODE=1

if [[ -f .env ]]; then
    source .env
fi

fastapi dev crud/main.py
