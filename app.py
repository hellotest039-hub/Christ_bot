import os
import sys
import traceback
from flask import Flask, render_template

# ==============================
# CONFIGURATION DES CHEMINS
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "ai"))
sys.path.insert(0, os.path.join(BASE_DIR, "scraper"))

# ==============================
# IMPORTS IA
# ==============================
from ai_models import (
    StatsAI,
    FormAI,
    H2HAI,
    ValueAI,
    CornersAI,
    HandicapAI,
    OverUnderAI,
    LearningAI
)

from ai_combinator import AICombinator
from bookmaker_sim import get_odds
from real_matches import get_real_matches
from fifa_virtual_matches import get_fifa_virtual_matches

# ==============================
# APP FLASK
# ==============================
app = Flask(__name__)
app.secret_key = "christ_bot_secret"

ais = [
    StatsAI(),
    FormAI(),
    H2HAI(),
    ValueAI(),
    CornersAI(),
    HandicapAI(),
    OverUnderAI(),
    LearningAI()
]

combinator = AICombinator()

# ==============================
# ROUTE PRINCIPALE
# ==============================
@app.route("/")
def dashboard():
    try:
        matches = get_real_matches() + get_fifa_virtual_matches()
        predictions = []

        for match in matches:
            odds_data = get_odds(match)
            ai_outputs = []

            for ai in ais:
                res = ai.analyze(match)
                res["odd"] = odds_data["markets"].get(
                    res["market"],
                    res.get("odd", 1.9)
                )
                ai_outputs.append(res)

            final_pred = combinator.combine(ai_outputs)
            predictions.append(final_pred)

        return render_template("dashboard.html", predictions=predictions)

    except Exception:
        traceback.print_exc()
        return "Erreur interne serveur", 500


# ==============================
# LOCAL ONLY
# ==============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
