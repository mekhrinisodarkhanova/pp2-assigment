import json
import os

FILE = "leaderboard.json"

def save_score(name, score):
    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append({"name": name, "score": score})

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(FILE, "w") as f:
        json.dump(data, f)