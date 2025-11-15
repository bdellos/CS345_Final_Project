import numpy as np
from data_loaders import load_tiny_sample
from data_loaders import features_used

def __main__():
    X,y = load_tiny_sample()
    feats = features_used()
    for i in range (len(feats)):
        print(f"{feats[i]} {X[0][i]}")

__main__()