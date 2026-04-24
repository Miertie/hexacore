def generate_report(tasks):
    filename = f"data/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

    return filename