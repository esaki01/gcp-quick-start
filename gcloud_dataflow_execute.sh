#!/usr/bin/env bash

gcloud dataflow jobs run myjob --gcs-location gs://dataflow-reference/template --parameters suffix=?
