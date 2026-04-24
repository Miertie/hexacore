#!/bin/bash

TARGET="$1"

if [ -z "$TARGET" ]; then
    echo "[ERROR] Usage: info_lookup.sh <query>"
    exit 1
fi

echo "[INFO] Basic OSINT lookup for: $TARGET"
echo "----------------------------------------"

echo "[Google Search suggestion]"
echo "https://www.google.com/search?q=$TARGET"

echo ""
echo "[Social search]"
echo "https://www.instagram.com/$TARGET"
echo "https://twitter.com/$TARGET"
echo "https://github.com/$TARGET"