#!/bin/bash

NAME="$1"
DOMAIN="$2"

if [ -z "$NAME" ] || [ -z "$DOMAIN" ]; then
    echo "[ERROR] Usage: email_guess.sh <name> <domain>"
    exit 1
fi

echo "[INFO] Email patterns for: $NAME@$DOMAIN"
echo "----------------------------------------"

echo "${NAME}@${DOMAIN}"
echo "${NAME}.official@${DOMAIN}"
echo "contact@${DOMAIN}"
echo "info@${DOMAIN}"
echo "${NAME}123@${DOMAIN}"
echo "${NAME}_dev@${DOMAIN}"