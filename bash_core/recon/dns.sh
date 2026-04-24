#!/bin/bash

TARGET="$1"

if [ -z "$TARGET" ]; then
    echo "[ERROR] Usage: dns.sh <domain>"
    exit 1
fi

echo "[INFO] DNS lookup for: $TARGET"
echo "----------------------------------------"

echo "[A RECORDS]"
dig +short A "$TARGET"

echo ""
echo "[NS RECORDS]"
dig +short NS "$TARGET"

echo ""
echo "[MX RECORDS]"
dig +short MX "$TARGET"