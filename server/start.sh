#!/usr/bin/env bash
source ./env/bin/activate

uvicorn main:app --reload --host 0.0.0.0 --port 4080
