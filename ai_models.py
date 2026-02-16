import random

class BaseAI:
    def analyze(self, match):
        return {}

# 1️⃣ Statistiques
class StatsAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Over 2.5",
            "prediction": "OVER",
            "odd": 1.80,
            "confidence": random.randint(65, 80)
        }

# 2️⃣ Forme récente
class FormAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "BTTS",
            "prediction": "YES",
            "odd": 1.85,
            "confidence": random.randint(68, 82)
        }

# 3️⃣ Head to Head
class H2HAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Double Chance",
            "prediction": "1X",
            "odd": 1.55,
            "confidence": random.randint(60, 75)
        }

# 4️⃣ Value betting
class ValueAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Value Bet",
            "prediction": "OVER 1.5",
            "odd": 2.10,
            "confidence": random.randint(70, 85)
        }

# 5️⃣ Corners
class CornersAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Corners Over 8.5",
            "prediction": "OVER",
            "odd": 1.90,
            "confidence": random.randint(65, 78)
        }

# 6️⃣ Handicap
class HandicapAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Handicap -1",
            "prediction": "HOME",
            "odd": 1.95,
            "confidence": random.randint(66, 80)
        }

# 7️⃣ Over / Under avancé
class OverUnderAI(BaseAI):
    def analyze(self, match):
        return {
            "match": match["match"],
            "market": "Under 3.5",
            "prediction": "UNDER",
            "odd": 1.60,
            "confidence": random.randint(70, 85)
        }
