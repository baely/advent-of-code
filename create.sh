#!/bin/bash

# Get current year and day
YEAR=$(date +%Y)
DAY=$(date +%d)

# Use command line argument if provided, otherwise use YEAR/DAY
TARGET_DIR=${1:-"$YEAR/$DAY"}

# Extract year and day from target directory
if [[ "$TARGET_DIR" =~ ([0-9]{4})/([0-9]{2}) ]]; then
    TARGET_YEAR="${BASH_REMATCH[1]}"
    TARGET_DAY="${BASH_REMATCH[2]}"
else
    echo "Error: TARGET_DIR must be in format YYYY/DD"
    exit 1
fi

# Check if directory already exists
if [ -d "$TARGET_DIR" ]; then
    # Directory exists - this is a subsequent run
    # Generate class names for part 1 and part 2
    CLASS_NAME_1="Solution${TARGET_DAY}01"
    CLASS_NAME_2="Solution${TARGET_DAY}02"

    # Check if we should copy Solution*01.java to Solution*02.java
    if [ -f "$TARGET_DIR/$CLASS_NAME_1.java" ] && { [ ! -f "$TARGET_DIR/$CLASS_NAME_2.java" ] || [ ! -s "$TARGET_DIR/$CLASS_NAME_2.java" ]; }; then
        cp "$TARGET_DIR/$CLASS_NAME_1.java" "$TARGET_DIR/$CLASS_NAME_2.java"
        # Replace class name in Solution*02.java
        sed -i '' "s/$CLASS_NAME_1/$CLASS_NAME_2/g" "$TARGET_DIR/$CLASS_NAME_2.java"
    fi
    # Open Solution*02.java in IntelliJ
    idea "$TARGET_DIR/$CLASS_NAME_2.java"
else
    # First run - create directory and copy template
    mkdir -p "$TARGET_DIR"

    # Generate class name for part 1
    CLASS_NAME_1="Solution${TARGET_DAY}01"

    # Copy template and replace placeholders
    cp ./template/Solution1.java "$TARGET_DIR/$CLASS_NAME_1.java"
    sed -i '' "s/Solution1/$CLASS_NAME_1/g" "$TARGET_DIR/$CLASS_NAME_1.java"
    sed -i '' "s|input.txt|./$TARGET_YEAR/$TARGET_DAY/input.txt|g" "$TARGET_DIR/$CLASS_NAME_1.java"

    cp ./template/input.txt "$TARGET_DIR/"

    # Open files in IntelliJ
    idea "$TARGET_DIR/input.txt"
    idea "$TARGET_DIR/$CLASS_NAME_1.java"
fi