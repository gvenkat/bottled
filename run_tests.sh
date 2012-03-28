#!/bin/bash

# if [ -e run_tests.py ]; then
#  echo "Can *NOT* find run_tests.py"
#  exit 1
# fi

SDK_ENV=/usr/local/google_appengine
TEST_PATH="$( pwd )/t/"

python run_tests.py $SDK_ENV $TEST_PATH



