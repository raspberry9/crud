#!/bin/bash
# override virtualenv directory
VIRTUALENV_DIR=.buildenv
# VIRTUALENV_ACTIVATE=${VIRTUALENV_DIR}/bin/activate

source scripts/common.sh

VIRTUALENV_DIR=${VIRTUALENV_DIR} scripts/devel/make_venv.sh



# if [[ ! -f ${VIRTUALENV_ACTIVATE} ]]; then
#     info Creating a virtual environment for build...
#     ${VIRTUALENV_BIN} -p ${PYTHON_BIN} ${VIRTUALENV_DIR}
# fi
