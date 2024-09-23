#!/bin/bash
source scripts/settings.sh

REQ_MD5_FILEPATH=${VIRTUALENV_DIR}/.requirements.md5

if [[ ! -f "${VIRTUALENV_BIN}" ]]; then
    error "virtualenv is not installed. Install it with the following command:\n\t${PYTHON_BIN} -m pip install virtualenv"
    exit 1
fi

if [[ ! -f ${VIRTUALENV_ACTIVATE} ]]; then
    info Creating a virtual environment...
    ${VIRTUALENV_BIN} -p ${PYTHON_BIN} ${VIRTUALENV_DIR}
fi

function install_packages() {
    source ${VIRTUALENV_ACTIVATE}; \
        INSTALL_TEST_PACKAGES=yes \
        scripts/build/install_packages.sh
    md5sum requirements/requirements.txt > ${REQ_MD5_FILEPATH}
    source ${VIRTUALENV_ACTIVATE}; pip freeze | md5sum >> ${REQ_MD5_FILEPATH}
}

function quit_if_requrements_remain_unchanged() {
    if [[ -f ${REQ_MD5_FILEPATH} ]]; then
        if [[ "`source ${VIRTUALENV_ACTIVATE}; pip freeze | md5sum requirements/requirements.txt -`" == "`cat ${REQ_MD5_FILEPATH}`" ]]; then
            # Requirements have not changed.
            exit 0
        else
            error "Requirements have changed. Reinstalling packages...:\n\tmake clean && make venv"
            exit 1
        fi
    fi
}

quit_if_requrements_remain_unchanged
install_packages
