#!/bin/bash
source scripts/common.sh
source ${VIRTUALENV_ACTIVATE}

export PYTHONDONTWRITEBYTECODE=1
export CRUD_DB_URL=sqlite:////tmp/_crud_test.db

trap 'rm -f /tmp/_crud_test.db' EXIT

pytest -vv -p no:cacheprovider
