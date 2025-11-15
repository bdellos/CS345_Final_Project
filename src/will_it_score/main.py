import numpy as np

from data_loaders import load_tiny_sample
from data_loaders import load_sample
from data_loaders import features_used

from models import multiple_splits

def __main__():
    X, y = load_sample()
    scores = multiple_splits(X,y,'logistic', 30)
    print(scores)

__main__()