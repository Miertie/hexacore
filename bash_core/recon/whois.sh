#!/bin/bash

TARGET="$1"

if [ -z "$TARGET" ]; then
    echo "[ERROR] Usage: whois.sh <domain>"
    exit 1
fi

echo "[INFO] Running WHOIS lookup for: $TARGET"
echo "----------------------------------------"

whois "$TARGET"