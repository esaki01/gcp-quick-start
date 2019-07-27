#!/usr/bin/env bash
gcloud composer environments storage dags import --environment example-environment --location asia-northeast1 --source src/composer/workflow.py
