#!/usr/bin/env bash

BUCKET_NAME=ai-platform-quick
JOB_NAME="my_first_keras_job"
JOB_DIR="gs://$BUCKET_NAME/keras-job-dir"
REGION="us-central1"

gcloud ai-platform jobs submit training ${JOB_NAME}_hpt \
  --config hptuning_config.yaml \
  --package-path trainer/ \
  --module-name trainer.task \
  --region $REGION \
  --python-version 3.5 \
  --runtime-version 1.13 \
  --job-dir $JOB_DIR \
  --stream-logs