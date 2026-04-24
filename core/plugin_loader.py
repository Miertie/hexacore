import os
import importlib

MODULES_PATH = "modules"

def load_modules():
    plugins = {}

    for file in os.listdir(MODULES_PATH):
        if file.endswith(".py") and file != "__init__.py":
            name = file[:-3]
            module = importlib.import_module(f"modules.{name}")
            plugins[name] = module

    return plugins