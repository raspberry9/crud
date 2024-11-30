#!/bin/bash

function check_requirements() {
    local requirements=("python3" "uvicorn")
    for req in ${requirements[@]}; do
        if [[ "`which $req`" == "" ]]; then
            echo "ERROR: $req is not installed. Please install it."
            exit 1
        fi
    done
}

check_requirements

# NOTE: Process count: os.cpu_count() * 2(sub processes) + 1(main process == uvicorn)
DEFAULT_CURD_WORKERS=`python3 -c "import os; print(os.cpu_count() * 2)"`

# variables
CRUD_PORT=${CRUD_PORT:-8000}
CURD_WORKERS=${CURD_WORKERS:-${DEFAULT_CURD_WORKERS}}

uvicorn crud.main:app \
        --log-config crud/conf/logging.prod.json \
        --port ${CRUD_PORT} \
        --workers=${CURD_WORKERS}