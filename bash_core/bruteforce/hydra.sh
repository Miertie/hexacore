#!/bin/bash

TARGET="$1"
SERVICE="$2"
USER="$3"
WORDLIST="$4"

if [ -z "$TARGET" ] || [ -z "$SERVICE" ] || [ -z "$USER" ] || [ -z "$WORDLIST" ]; then
    echo "[ERROR] Usage: hydra.sh <target> <service> <user> <wordlist>"
    exit 1
fi

echo "[INFO] Starting Hydra attack..."
echo "Target: $TARGET"
echo "Service: $SERVICE"
echo "User: $USER"
echo "Wordlist: $WORDLIST"
echo "----------------------------------------"

hydra -l "$USER" -P "$WORDLIST" "$TARGET" "$SERVICE"