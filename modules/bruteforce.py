from core.router import bruteforce

def hydra(target, service, user, wordlist):
    return bruteforce("hydra", target, service, user, wordlist)

def john(file):
    return bruteforce("john", file)