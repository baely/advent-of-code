#!/bin/bash

# Get current year and day
YEAR=$(date +%Y)
DAY=$(date +%d)

# Use command line argument if provided, otherwise use YEAR/DAY
TARGET_DIR=${1:-"$YEAR/$DAY"}

# Check if directory already exists
if [ -d "$TARGET_DIR" ]; then
    # Directory exists - this is a subsequent run
    # Check if we should copy Solution1.java to Solution2.java
    if [ -f "$TARGET_DIR/Solution1.java" ] && { [ ! -f "$TARGET_DIR/Solution2.java" ] || [ ! -s "$TARGET_DIR/Solution2.java" ]; }; then
        cp "$TARGET_DIR/Solution1.java" "$TARGET_DIR/Solution2.java"
        # Replace class name in Solution2.java
        sed -i '' 's/Solution1/Solution2/g' "$TARGET_DIR/Solution2.java"
    fi
    # Open Solution2.java in IntelliJ
    idea "$TARGET_DIR/Solution2.java"
else
    # First run - create directory and copy template
    mkdir -p "$TARGET_DIR"
    cp ./template/Solution1.java "$TARGET_DIR/"
    cp ./template/input.txt "$TARGET_DIR/"
    # Open Solution1.java in IntelliJ
    idea "$TARGET_DIR/input.txt"
    idea "$TARGET_DIR/Solution1.java"
fi