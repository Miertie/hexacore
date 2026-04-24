#!/bin/bash

BASE="$1"

if [ -z "$BASE" ]; then
    echo "[ERROR] Usage: username_gen.sh <name>"
    exit 1
fi

echo "[INFO] Username variations for: $BASE"
echo "----------------------------------------"

echo "${BASE}"
echo "${BASE}123"
echo "${BASE}_pro"
echo "real${BASE}"
echo "${BASE}x"
echo "${BASE}_official"
echo "${BASE}007"
echo "${BASE}dev"