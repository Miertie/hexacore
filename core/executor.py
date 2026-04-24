import subprocess
from core.logger import log

def run(module, tool, *args):
    cmd = f"bash bash_core/main.sh {module} {tool} {' '.join(args)}"

    log("EXECUTE", cmd)

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    return {
        "command": cmd,
        "output": result.stdout,
        "error": result.stderr,
        "code": result.returncode
    }