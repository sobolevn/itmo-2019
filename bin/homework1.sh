#!/usr/bin/env bash

set -e

for runtests in $(find students/*/1 -maxdepth 3 -name 'runtests.py'); do
  python "$runtests"
done
