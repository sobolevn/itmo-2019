#!/usr/bin/env bash

set -e

pyclean () {
  # Cleans py[cod] and __pychache__ dirs in the current tree:
  find . | grep -E "(__pycache__|\.py[cod]$)" | xargs rm -rf
}

for dir in $(find students -mindepth 1 -maxdepth 1 -type d); do
  echo "Running tests for: $dir"
  pytest "$dir"
  pyclean
  echo
done
