#!/bin/bash
CRUD_PORT=${CRUD_PORT:-8000}
WORKERS=`python3 -c "import os; print(os.cpu_count() * 2 + 1)"`

fastapi run crud/main.py --workers=${WORKERS}
