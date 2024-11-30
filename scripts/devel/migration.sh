#!/bin/bash
source scripts/common.sh

source ${VIRTUALENV_ACTIVATE}

check_requirements alembic

function check_alembic() {
    if [[ ! -d "alembic/versions" ]]; then
        error "Alembic is not initialized. Run 'alembic init alembic' first."
        exit 1
    fi
    if [[ "`find alembic/versions -type f -name *.py`" == "" ]]; then
        error "Alembic has no migration scripts. Run 'alembic revision --autogenerate -m \"Initial migration\"' first."
        exit 1
    fi
}

check_alembic

alembic upgrade head