class AICombinator:
    def combine(self, outputs):
        if not outputs:
            return {"status": "no_prediction"}

        best = max(outputs, key=lambda x: x["confidence"])

        return {
            "status": "ok",
            "match": best["match"],
            "market": best["market"],
            "prediction": best["prediction"],
            "odd": best["odd"],
            "confidence": best["confidence"]
        }
