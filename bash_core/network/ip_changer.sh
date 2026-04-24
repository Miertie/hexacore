#!/bin/bash

IFACE="$1"

if [ -z "$IFACE" ]; then
    echo "[ERROR] Usage: ip_changer.sh <interface>"
    exit 1
fi

echo "[INFO] Restarting network interface: $IFACE"
echo "----------------------------------------"

# сброс интерфейса
sudo ip link set "$IFACE" down

# получение нового IP через DHCP
sudo dhclient -r "$IFACE"
sudo dhclient "$IFACE"

echo "[SUCCESS] IP renewed for $IFACE"