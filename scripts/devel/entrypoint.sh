#!/bin/bash
source scripts/common.sh
source ${VIRTUALENV_ACTIVATE}

export PYTHONDONTWRITEBYTECODE=1

# variables
CRUD_DEBUG=${CRUD_DEBUG:-0}
CRUD_PORT=${CRUD_PORT:-8000}

# load .env file
if [[ -f .env ]]; then
    set -a  # automatically export all variables
    source .env
    set +a
fi

if [[ "${CRUD_DEBUG}" == "1" ]]; then
    echo "Running in debug mode..."
    uvicorn crud.main:app \
        --log-config crud/conf/logging.dev.json \
        --port ${CRUD_PORT} \
        --reload
    exit 0
else
    uvicorn crud.main:app \
        --log-config crud/conf/logging.prod.json \
        --port ${CRUD_PORT}
fi
