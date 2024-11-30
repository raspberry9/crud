#!/bin/bash
source scripts/common.sh
source ${VIRTUALENV_ACTIVATE}

# variables
# -----------------------------------------------------------------------------
set -a # automatically export all variables
PYTHONDONTWRITEBYTECODE=1 # disable writing .pyc files
CRUD_DEBUG=${CRUD_DEBUG:-1} # 1: debug mode, 0: production mode
CRUD_PORT=${CRUD_PORT:-8000} # port number
CRUD_DB_URL=${CRUD_DB_URL:-sqlite:///./debug.db} # database URL
# load .env file if exists
if [[ -f .env ]]; then
    source .env
fi
set +a # stop exporting variables
# -----------------------------------------------------------------------------

check_requirements python3.12 uvicorn

if [[ "${CRUD_DEBUG}" == "1" ]]; then
    echo "Running in debug mode..."
    uvicorn crud.main:app \
        --log-config crud/conf/logging.dev.json \
        --port ${CRUD_PORT} \
        --reload
else
    # Running in production mode..."
    uvicorn crud.main:app \
        --log-config crud/conf/logging.prod.json \
        --port ${CRUD_PORT}
fi
