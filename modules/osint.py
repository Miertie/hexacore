from core.router import osint

def username_gen(name):
    return osint("username_gen", name)

def email_guess(name, domain):
    return osint("email_guess", name, domain)

def info_lookup(query):
    return osint("info_lookup", query)