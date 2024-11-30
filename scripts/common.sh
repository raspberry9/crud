#!/bin/bash
set -eu
# settings
# -----------------------------------------------------------------------------
PYTHON_VERSION=3.12
PYTHON_BIN=/usr/local/bin/python${PYTHON_VERSION} # ex) /usr/local/bin/python3.12
VIRTUALENV_DIR=.venv
VIRTUALENV_ACTIVATE=${VIRTUALENV_DIR}/bin/activate # ex) .venv/bin/activate
# -----------------------------------------------------------------------------

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
    # usage: info "info message"
    echo -e "${FG_BLUE}[i] $@${FG_RESET}"
}

function warn() {
    # usage: warn "warn message"
    local message=${1}
    echo -e "${FG_YELLOW}[W] $@${FG_RESET}" 1>&2
}

function error() {
    # usage: error "error message"
    local message=${1}
    echo -e "${FG_RED}[E] $@${FG_RESET}" 1>&2
}

function check_requirements() {
    local requirements=${@}
    for req in ${requirements[@]}; do
        if [[ "`which $req`" == "" ]]; then
            if [[ ! -f "${req}" ]]; then
                error "${req} is not installed. Please install it."
                exit 1
            fi
        fi
    done
}

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
        error "Unsupported OS: ${OS_PLATFORM}"
        exit 1
        ;;
esac

check_requirements ${PYTHON_BIN} ${VIRTUALENV_BIN}
