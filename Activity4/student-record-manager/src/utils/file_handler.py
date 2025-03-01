def load_records(filename):
    import json
    import os

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_records(filename, records):
    import json

    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)