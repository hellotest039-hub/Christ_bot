import os
import sys
import traceback
from flask import Flask, render_template

# =========================================
# CONFIGURATION DES CHEMINS (RENDER SAFE)
# =========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

AI_DIR = os.path.join(BASE_DIR, "ai")
SCRAPER_DIR = os.path.join(BASE_DIR, "scraper")

if AI_DIR not in sys.path:
    sys.path.insert(0, AI_DIR)

if SCRAPER_DIR not in sys.path:
    sys.path.insert(0, SCRAPER_DIR)

# =========================================
# IMPORTS (NE PAS MODIFIER)
# =========================================
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

# =========================================
# APP FLASK
# =========================================
app = Flask(__name__)
app.secret_key = "christ_bot_secret_key"

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

# =========================================
# ROUTE PRINCIPALE
# =========================================
@app.route("/")
def dashboard():
    try:
        matches = []

        real_matches = get_real_matches()
        virtual_matches = get_fifa_virtual_matches()

        if real_matches:
            matches.extend(real_matches)
        if virtual_matches:
            matches.extend(virtual_matches)

        predictions = []

        for match in matches:
            if "match" not in match:
                continue

            odds_data = get_odds(match)
            ai_results = []

            for ai in ais:
                res = ai.analyze(match)

                if not isinstance(res, dict):
                    continue

                market = res.get("market")
                if market in odds_data["markets"]:
                    res["odd"] = odds_data["markets"][market]

                ai_results.append(res)

            if ai_results:
                final_prediction = combinator.combine(ai_results)
                predictions.append(final_prediction)

        return render_template("dashboard.html", predictions=predictions)

    except Exception:
        # AFFICHAGE COMPLET DE L'ERREUR (IMPORTANT)
        return f"<pre>{traceback.format_exc()}</pre>", 500


# =========================================
# LANCEMENT (OBLIGATOIRE POUR RENDER)
# =========================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
