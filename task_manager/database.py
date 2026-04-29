import json
import os

DB_FILE = "tasks.json"
tasks = []

def load_data():
    global tasks
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            tasks.extend(json.load(f))

def save_data():
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

load_data() # Load immediately on import