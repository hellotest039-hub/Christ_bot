from datetime import datetime, timedelta

COMPETITIONS = [
    "Premier League",
    "La Liga",
    "Serie A",
    "Bundesliga",
    "Ligue 1",
    "Champions League",
    "Europa League",
    "Match Amical"
]

def get_real_matches():
    """
    Génère les matchs réels sur 3 jours
    (structure prête pour scraping réel plus tard)
    """
    matches = []
    today = datetime.now()

    for day_offset in range(3):
        match_date = today + timedelta(days=day_offset)
        date_str = match_date.strftime("%Y-%m-%d")

        for i, comp in enumerate(COMPETITIONS):
            matches.append({
                "date": date_str,
                "type": "real",
                "competition": comp,
                "match": f"{comp} Team {i+1} vs Team {i+2}"
            })

    return matches
