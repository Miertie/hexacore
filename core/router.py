from core.executor import run

def recon(tool, target):
    return run("recon", tool, target)

def bruteforce(tool, *args):
    return run("bruteforce", tool, *args)

def network(tool, *args):
    return run("network", tool, *args)

def osint(tool, *args):
    return run("osint", tool, *args)

def exploit(tool, *args):
    return run("exploit", tool, *args)

def execute(module, tool, *args):
    return run(module, tool, *args)