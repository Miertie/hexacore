import uuid
from core.router import execute

TASKS = {}

def create_task(module, tool, *args):
    task_id = str(uuid.uuid4())

    TASKS[task_id] = {
        "status": "running",
        "module": module,
        "tool": tool,
        "result": None
    }

    try:
        result = execute(module, tool, *args)
        TASKS[task_id]["status"] = "done"
        TASKS[task_id]["result"] = result
    except Exception as e:
        TASKS[task_id]["status"] = "error"
        TASKS[task_id]["result"] = str(e)

    return task_id

def get_task(task_id):
    return TASKS.get(task_id, None)