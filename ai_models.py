import os
import json
import random

HISTO_FILE = "ai_history.json"

# ----------------- IA STATISTIQUES -----------------
class StatsAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "1X2",
            "prediction": random.choice(["HOME", "DRAW", "AWAY"]),
            "odd": round(random.uniform(1.5, 3.5), 2),
            "confidence": random.randint(60, 80)
        }

# ----------------- FORM / PERFORMANCE -----------------
class FormAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Over 2.5",
            "prediction": "OVER" if random.random() > 0.5 else "UNDER",
            "odd": round(random.uniform(1.6, 2.2), 2),
            "confidence": random.randint(55, 75)
        }

# ----------------- HISTORIQUE FACE-A-FACE -----------------
class H2HAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "BTTS",
            "prediction": "YES" if random.random() > 0.5 else "NO",
            "odd": round(random.uniform(1.7, 2.0), 2),
            "confidence": random.randint(50, 70)
        }

# ----------------- VALUE / COTES -----------------
class ValueAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Corners Over 8.5",
            "prediction": "OVER",
            "odd": round(random.uniform(1.8, 2.1), 2),
            "confidence": random.randint(55, 75)
        }

# ----------------- CORNERS -----------------
class CornersAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Corners Over 8.5",
            "prediction": "OVER" if random.random() > 0.5 else "UNDER",
            "odd": round(random.uniform(1.8, 2.2), 2),
            "confidence": random.randint(50, 70)
        }

# ----------------- HANDICAP -----------------
class HandicapAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Handicap -1",
            "prediction": "HOME",
            "odd": round(random.uniform(1.9, 2.3), 2),
            "confidence": random.randint(55, 75)
        }

# ----------------- OVER / UNDER -----------------
class OverUnderAI:
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Over 2.5",
            "prediction": "OVER" if random.random() > 0.5 else "UNDER",
            "odd": round(random.uniform(1.6, 2.2), 2),
            "confidence": random.randint(50, 70)
        }

# ----------------- IA AUTO-APPRENANTE -----------------
class LearningAI:
    def __init__(self):
        if os.path.exists(HISTO_FILE):
            with open(HISTO_FILE, "r") as f:
                self.history = json.load(f)
        else:
            self.history = {}

    def analyze(self, match):
        base_conf = random.randint(65, 85)
        key = match["match"]
        if key in self.history:
            base_conf += self.history[key].get("success_bonus", 0)
            base_conf = min(base_conf, 95)
        return {
            "match": key,
            "market": "Learning Over 2.5",
            "prediction": "OVER",
            "odd": 1.88,
            "confidence": base_conf
        }

    def update_history(self, match, correct):
        key = match["match"]
        bonus = 5 if correct else -3
        if key not in self.history:
            self.history[key] = {"success_bonus": 0}
        self.history[key]["success_bonus"] += bonus
        with open(HISTO_FILE, "w") as f:
            json.dump(self.history, f)
