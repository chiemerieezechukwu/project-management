#!/bin/bash
set -xe

SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

cd $SCRIPT_DIR && echo "Inside Script directory"

bash setup.sh || exit 1

cd ..

pytest --cov-report=term-missing --cov=crowdmoni --disable-network -x --cov-fail-under=90

echo "writing coverage..."

coverage html

deactivate
