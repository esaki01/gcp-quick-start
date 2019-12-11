#!/usr/bin/env bash

REGION="us-central1"
MODEL_NAME="my_first_keras_model"

gcloud ai-platform models create $MODEL_NAME \
  --regions $REGION