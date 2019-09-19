#!/usr/bin/env bash

set -e

if [ -f 'students/runtests.py' ]; then
  echo "runtests.py exist in the root students/ folder!"
  exit 1
fi

for homework_folder1 in $(find students/* -maxdepth 1 -name 1); do
  if [ ! -f "$homework_folder1/runtests.py" ]; then
    echo "runtests.py does not exist in $homework_folder1"
    exit 1
  fi
done

for runtests in $(find students/*/1 -maxdepth 1 -name 'runtests.py'); do
  poetry run python "$runtests"
done
