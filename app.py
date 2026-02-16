from flask import Flask, render_template
import sys, os, traceback
import random
import json

# --- CONFIG CHEMIN ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "ai"))
sys.path.append(os.path.join(BASE_DIR, "scraper"))

# --- IMPORT DES IA ---
from ai_models import (
    StatsAI, FormAI, H2HAI, ValueAI,
    CornersAI, HandicapAI, OverUnderAI, LearningAI
)
from ai_combinator import AICombinator

# --- IMPORT DES MATCHES SIMULÉS ---
# Remplace avec tes fonctions réelles
from fifa_virtual_matches import get_fifa_virtual_matches
from real_matches import get_real_matches
from scraper.bookmaker_sim import get_odds

# --- INIT FLASK ---
app = Flask(__name__)
app.secret_key = "christ_bot_secret"

# --- INIT IA ---
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

# --- ROUTE DASHBOARD ---
@app.route("/")
def dashboard():
    try:
        matches = get_real_matches() + get_fifa_virtual_matches()
        predictions = []

        for match in matches:
            odds_data = get_odds(match)
            outputs = []

            for ai in ais:
                res = ai.analyze(match)
                # met à jour la côte simulée si le marché existe
                res["odd"] = odds_data["markets"].get(res["market"], res["odd"])
                outputs.append(res)

            if outputs:
                predictions.append(combinator.combine(outputs))

        return render_template("dashboard.html", predictions=predictions)

    except Exception:
        traceback.print_exc()
        return "Erreur interne", 500

# --- LANCEMENT RENDER / LOCAL ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
