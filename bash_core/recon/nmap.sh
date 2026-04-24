#!/bin/bash

TARGET="$1"

if [ -z "$TARGET" ]; then
    echo "[ERROR] Usage: nmap.sh <target>"
    exit 1
fi

echo "[INFO] Running NMAP scan on: $TARGET"
echo "----------------------------------------"

nmap -sV "$TARGET"