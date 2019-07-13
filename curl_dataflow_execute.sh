#!/usr/bin/env bash

curl -X POST -H "Content-Type: application/json" -d '{"jobName": "myjob", "parameters": {"suffix" : "?",}, "environment": {"tempLocation": "gs://dataflow-reference/tmp", "zone": "us-central1-f"}}
' https://dataflow.googleapis.com/v1b3/projects/dataflow-reference/templates:launch?gcsPath=gs://dataflow-reference/template
