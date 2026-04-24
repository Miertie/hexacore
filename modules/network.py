from core.router import network

def mac_changer(iface, mac):
    return network("mac_changer", iface, mac)

def ip_changer(iface):
    return network("ip_changer", iface)

def ip_info():
    return network("ip_info")

def wifi_scan(iface):
    return network("wifi_scan", iface)