#!/bin/sh

if [ "$#" -eq 2 ]; then
    python3 rushhour.py "$1" "$2"
elif [ "$#" -eq 1 ]; then
    python3 rushhour.py "$1"
else
    echo "run.sh <command> [<optional-argument>]"
fi
