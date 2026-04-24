#!/bin/bash

# =========================
# MR Tool Core Router
# =========================

CATEGORY="$1"
TOOL="$2"
shift 2

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$BASE_DIR/$CATEGORY/$TOOL.sh"

# Проверка аргументов
if [ -z "$CATEGORY" ] || [ -z "$TOOL" ]; then
    echo "[ERROR] Usage: main.sh <category> <tool> <args...>"
    exit 1
fi

# Проверка существования инструмента
if [ ! -f "$SCRIPT" ]; then
    echo "[ERROR] Tool not found: $CATEGORY/$TOOL.sh"
    exit 1
fi
bash bash_core/main.sh exploit search apache
bash bash_core/main.sh exploit detail "linux/remote/12345"

# Запуск инструмента с передачей всех аргументов
bash "$SCRIPT" "$@"