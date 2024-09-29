#!/bin/bash
source scripts/common.sh

info Installing packages...
python -m pip install -r requirements/requirements.txt

if [[ "${INSTALL_TEST_PACKAGES}" == "yes" ]]; then
    info Installing test packages...
    python -m pip install -r requirements/test_requirements.txt
fi
