import random

def get_odds(match):
    """
    Simulation de cotes type bookmaker
    """
    return {
        "match": match["match"],
        "markets": {
            "1X2": round(random.uniform(1.5, 3.5), 2),
            "Over 2.5": round(random.uniform(1.6, 2.2), 2),
            "BTTS": round(random.uniform(1.7, 2.0), 2),
            "Corners Over 8.5": round(random.uniform(1.8, 2.2), 2),
            "Handicap -1": round(random.uniform(1.9, 2.3), 2),
            "Learning Over 2.5": round(random.uniform(1.7, 2.1), 2)
        }
    }
