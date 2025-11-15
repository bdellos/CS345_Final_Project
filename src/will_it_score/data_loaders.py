"""
File to be used for data imports. Should keep our code cleaner this way.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
COLS = ["shotID", "isPlayoffGame", "time", "homeTeamGoals", "awayTeamGoals",
        "shotAngle", "shotDistance", "shotOnEmptyNet", "shotRebound", "shotRush",
        "shooterTimeOnIce", "offWing"]
TARGET = ["goal"] # usecols expects an iterable object

def features_used():
    return COLS.copy()

def load_tiny_sample():
    file = ROOT / "resources/tiny_shots_2025.csv"
    data = pd.read_csv(file, delimiter=',', usecols=COLS+TARGET, header=0)
    features = data[COLS].to_numpy()
    labels   = data[TARGET].to_numpy()
    return features, labels
