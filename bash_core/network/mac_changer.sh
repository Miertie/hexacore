#!/bin/bash

IFACE="$1"
NEW_MAC="$2"

if [ -z "$IFACE" ] || [ -z "$NEW_MAC" ]; then
    echo "[ERROR] Usage: mac_changer.sh <interface> <new_mac>"
    exit 1
fi

echo "[INFO] Changing MAC address..."
echo "Interface: $IFACE"
echo "New MAC: $NEW_MAC"
echo "----------------------------------------"

sudo ip link set "$IFACE" down
sudo ip link set "$IFACE" address "$NEW_MAC"
sudo ip link set "$IFACE" up

echo "[SUCCESS] MAC changed"