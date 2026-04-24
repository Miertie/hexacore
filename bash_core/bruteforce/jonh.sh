#!/bin/bash

FILE="$1"

if [ -z "$FILE" ]; then
    echo "[ERROR] Usage: john.sh <hash_file>"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "[ERROR] File not found: $FILE"
    exit 1
fi

echo "[INFO] Starting John the Ripper..."
echo "File: $FILE"
echo "----------------------------------------"

john "$FILE"

echo ""
echo "[INFO] Showing cracked results:"
john --show "$FILE"