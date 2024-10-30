#!/bin/bash

# Get current year and day
YEAR=$(date +%Y)
DAY=$(date +%d)

# Use command line argument if provided, otherwise use YEAR/DAY
TARGET_DIR=${1:-"$YEAR/$DAY"}

# Check if directory already exists
if [ -d "$TARGET_DIR" ]; then
    # Directory exists - this is a subsequent run
    # Check if we should copy 1.py to 2.py
    if [ -f "$TARGET_DIR/1.py" ] && { [ ! -f "$TARGET_DIR/2.py" ] || [ ! -s "$TARGET_DIR/2.py" ]; }; then
        cp "$TARGET_DIR/1.py" "$TARGET_DIR/2.py"
    fi
    # Open 2.py in PyCharm
    pycharm "$TARGET_DIR/2.py"
else
    # First run - create directory and copy template
    mkdir -p "$TARGET_DIR"
    cp -r ./template/. "$TARGET_DIR/"
    # Open 1.py in PyCharm
    pycharm "$TARGET_DIR/input.txt"
    pycharm "$TARGET_DIR/1.py"
fi