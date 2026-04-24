#!/bin/bash

DOMAIN="$1"

if [ -z "$DOMAIN" ]; then
    echo "[ERROR] Usage: subdomain.sh <domain>"
    exit 1
fi

echo "[INFO] Subdomain enumeration for: $DOMAIN"
echo "----------------------------------------"

# базовый wordlist (можешь потом расширить)
WORDLIST=("www" "mail" "ftp" "api" "dev" "test" "admin" "portal")

for sub in "${WORDLIST[@]}"; do
    HOST="${sub}.${DOMAIN}"
    
    IP=$(dig +short "$HOST")

    if [ ! -z "$IP" ]; then
        echo "[FOUND] $HOST -> $IP"
    fi
done