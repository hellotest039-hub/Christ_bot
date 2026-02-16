from flask import Flask, render_template
import sys, os, traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "ai"))
sys.path.append(os.path.join(BASE_DIR, "scraper"))

from ai_models import StatsAI, FormAI
from ai_combinator import AICombinator
from real_matches import get_real_matches
from fifa_virtual_matches import get_fifa_virtual_matches

app = Flask(__name__)
app.secret_key = "christustips"

ais = [StatsAI(), FormAI()]
combinator = AICombinator()

@app.route("/")
def dashboard():
    try:
        matches = get_real_matches() + get_fifa_virtual_matches()
        predictions = []

        for match in matches:
            outputs = []
            for ai in ais:
                res = ai.analyze(match)
                if res:
                    outputs.append(res)

            if outputs:
                predictions.append(combinator.combine(outputs))

        return render_template("dashboard.html", predictions=predictions)

    except Exception:
        traceback.print_exc()
        return "Erreur interne", 500


if __name__ == "__main__":
    app.run(debug=True)
