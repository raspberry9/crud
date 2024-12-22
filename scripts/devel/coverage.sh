#!/bin/bash
source scripts/common.sh

source ${VIRTUALENV_ACTIVATE}

check_requirements coverage pytest

export CRUD_DB_URL=sqlite:////tmp/_crud_coverage.db

trap 'rm -f /tmp/_crud_coverage.db' EXIT

coverage run -m pytest
coverage report -m
