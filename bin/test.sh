#!/usr/bin/env bash

set -e

pyclean () {
  # Cleans py[cod] and __pychache__ dirs in the current tree:
  find . | grep -E "(__pycache__|\.py[cod]$)" | xargs rm -rf
}

for dir in $(find students -type d -mindepth 1 -maxdepth 1); do
  echo "Running tests for: $dir"
  pytest "$dir"
  pyclean
done
