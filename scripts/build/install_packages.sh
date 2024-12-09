#!/bin/bash
source scripts/common.sh

info Installing packages...
python -m pip install -r requirements/requirements.txt

if [[ "${INSTALL_TEST_PACKAGES}" == "yes" ]]; then
    info Installing test packages...
    python -m pip install -r requirements/test_requirements.txt
fi

if [[ "${INSTALL_DEV_PACKAGES}" == "yes" ]]; then
    info Installing dev packages...
    python -m pip install -r requirements/dev_requirements.txt
fi

if [[ "${INSTALL_BUILD_PACKAGES}" == "yes" ]]; then
    info Installing build packages...
    python -m pip install -r requirements/build_requirements.txt
fi
