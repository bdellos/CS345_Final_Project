"""
File to be used for data imports. Should keep our code cleaner this way.
"""
from pathlib import Path
import pandas as pd
import sklearn as skl


ROOT = Path(__file__).resolve().parents[2]
COLS = ["shotID", "isPlayoffGame", "time", "homeTeamGoals", "awayTeamGoals",
        "shotAngle", "shotDistance", "shotOnEmptyNet", "shotRebound", "shotRush",
        "shooterTimeOnIce", "offWing"]
TARGET = ["goal"] # usecols expects an iterable object
NUMER = ["shotID", "time", "homeTeamGoals", "awayTeamGoals", "shotAngle", "shotDistance",
         "shooterTimeOnIce"]
BINARY = ["isPlayoffGame", "shotOnEmptyNet", "shotRebound", "shotRush", "offWing"]
ONEHOT = []

def features_used():
    return COLS.copy()

def load_tiny_sample():
    file = ROOT / "resources/tiny_shots_2025.csv"
    data = pd.read_csv(file, delimiter=',', usecols=COLS+TARGET, header=0)
    features = data[COLS].to_numpy()
    labels   = data[TARGET].to_numpy().squeeze() # squeeze to get rid of data conversion error
    return features, labels

def load_sample():
    file = ROOT / "resources/shots_2025.csv"    # FILE PULLED 11/11
    data = pd.read_csv(file, delimiter=',', usecols=COLS+TARGET, header=0)
    features = data[COLS].to_numpy()
    labels   = data[TARGET].to_numpy().squeeze() # squeeze to get rid of data conversion error
    return features, labels
