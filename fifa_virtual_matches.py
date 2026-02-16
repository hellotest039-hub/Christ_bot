import random
from datetime import datetime

FIFA_LEAGUES = [
    "FIFA 5x5 Rush",
    "FIFA 4x4",
    "FIFA 3x3",
    "FIFA Virtual Arena"
]

def get_fifa_virtual_matches():
    matches = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    for league in FIFA_LEAGUES:
        for i in range(4):
            matches.append({
                "date": now,
                "type": "virtual",
                "competition": league,
                "match": f"Virtual Team {random.randint(1,20)} vs Virtual Team {random.randint(1,20)}"
            })

    return matches
