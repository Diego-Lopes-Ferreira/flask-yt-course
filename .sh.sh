#!/bin/bash

# prints the input
function print() {
  echo 'Your input: ' $1
}

function run() {
  if [ "$1" = "venv" ]; then
    echo "Initiating VENV"
    echo "source venv/Scripts/activate"
    echo ""
    source venv/Scripts/activate
  else
    echo "Initiating Server"
    echo "py ./run.py runserver"
    echo ""
    py ./run.py runserver
  fi
}
