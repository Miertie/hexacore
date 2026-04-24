from core.router import recon

def whois(target):
    return recon("whois", target)

def nmap(target):
    return recon("nmap", target)

def dns(target):
    return recon("dns", target)

def subdomain(target):
    return recon("subdomain", target)