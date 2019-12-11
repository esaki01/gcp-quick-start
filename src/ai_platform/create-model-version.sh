#!/usr/bin/env bash

BUCKET_NAME=ai-platform-quick
JOB_DIR="gs://$BUCKET_NAME/keras-job-dir"
REGION="us-central1"

MODEL_NAME="my_first_keras_model"
MODEL_VERSION="v1"

# Get a list of directories in the `keras_export` parent directory. Then pick
# the directory with the latest timestamp, in case you've trained multiple
# times.
SAVED_MODEL_PATH=$(gsutil ls $JOB_DIR/keras_export | tail -n 1)

# Create model version based on that SavedModel directory
gcloud ai-platform versions create $MODEL_VERSION \
  --model $MODEL_NAME \
  --runtime-version 1.13 \
  --python-version 3.5 \
  --framework tensorflow \
  --origin $SAVED_MODEL_PATH