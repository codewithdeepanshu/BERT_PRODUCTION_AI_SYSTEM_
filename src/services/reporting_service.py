import csv
from pathlib import Path

def export_predictions_to_csv(tweet_id: str, predictions, out_dir: str = "exports"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    path = Path(out_dir) / f"{tweet_id}_analysis.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "sentiment", "confidence"])
        writer.writeheader()
        writer.writerows(predictions)
    return str(path)
