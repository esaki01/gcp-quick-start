#!/usr/bin/env bash

MODEL_NAME="my_first_keras_model"
MODEL_VERSION="v1"

gcloud ai-platform predict \
  --model $MODEL_NAME \
  --version $MODEL_VERSION \
  --json-instances prediction_input.json
