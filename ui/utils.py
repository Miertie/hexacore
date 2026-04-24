def format_result(result):
    if isinstance(result, dict):
        output = result.get("output", "")
        error = result.get("error", "")

        if error:
            return f"[ERROR]\n{error}\n\n[OUTPUT]\n{output}"

        return output

    return str(result)