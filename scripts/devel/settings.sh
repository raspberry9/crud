#!/bin/bash
set -eu

FG_RESET='\033[0m'
FG_BLACK='\033[0;30m'
FG_RED='\033[0;31m'
FG_GREEN='\033[0;32m'
FG_YELLOW='\033[0;33m'
FG_BLUE='\033[0;34m'
FG_PURPLe='\033[0;35m'
FG_CYAN='\033[0;36m'
FG_WHITE='\033[0;37m'

function info() {
    echo -e "${FG_BLUE}[i] $@${FG_RESET}"
}

function warn() {
    local message=${1}
    echo -e "${FG_YELLOW}[W] $@${FG_RESET}" 1>&2
}

function error() {
    local message=${1}
    echo -e "${FG_RED}[E] $@${FG_RESET}" 1>&2
}

# Python
PYTHON_VERSION=3.12
PYTHON_BIN=/usr/local/bin/python${PYTHON_VERSION}

# Check requirements
if [[ "`which ${PYTHON_BIN}`" == "" ]]; then
    echo "Python ${PYTHON_VERSION} is not installed. Please install it."
    exit 1
fi

VIRTUALENV_DIR=.venv
VIRTUALENV_ACTIVATE=${VIRTUALENV_DIR}/bin/activate

OS_PLATFORM="`uname -s`"
case "${OS_PLATFORM}" in
    "Darwin")
        # ex) /System/Volumes/Data/Library/Frameworks/Python.framework/Versions/3.12/bin/virtualenv
        VIRTUALENV_BIN="/System/Volumes/Data/Library/Frameworks/Python.framework/Versions/${PYTHON_VERSION}/bin/virtualenv"
        ;;
    "Linux")
        # ex) ${HOME}/.local/bin/virtualenv
        VIRTUALENV_BIN="${HOME}/.local/bin/virtualenv"
        ;;
    *)
        echo "Unsupported OS: ${OS_PLATFORM}"
        exit 1
        ;;
esac

# virtualenv
if [[ ! -f "${VIRTUALENV_BIN}" ]]; then
    error "virtualenv is not installed. Please install it.\n\t ${PYTHON_BIN} -m pip install virtualenv"
    exit 1
fi