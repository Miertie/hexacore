#!/bin/bash

IFACE="$1"

if [ -z "$IFACE" ]; then
    echo "[ERROR] Usage: wifi_scan.sh <interface>"
    exit 1
fi

echo "[INFO] Scanning WiFi networks..."
echo "Interface: $IFACE"
echo "----------------------------------------"

sudo iwlist "$IFACE" scan | grep -E "ESSID|Signal|Quality"