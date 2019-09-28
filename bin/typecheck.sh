#!/usr/bin/env bash

set -e

for dir in $(find students/* -mindepth 1 -maxdepth 1 -type d); do
  homework_number=$(basename "$dir")

  if [ "$homework_number" -ge 4 ]; then
    echo "Typechecking $dir"
    mypy "$dir"
  else
    echo "Skipping $dir"
  fi

  echo
done
