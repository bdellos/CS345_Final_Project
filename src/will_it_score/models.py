"""
File to create data loaders in. Again, should keep code
cleaner, especially as we incorporate more models.
"""
import time

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


# so we can pass a model type in and return the appropriate pipeline for that model
def build_model(model_type):
    if model_type == 'logistic':
        return Pipeline([
            ("scaler", StandardScaler()),
            ("logreg", LogisticRegression())
        ])
    """
    TODO: implement other model types here
    """
    raise ValueError(f"Unknown model type {model_type}")

# so we can evaluate scores over multiple iterations for better "true" accuracy
def multiple_splits(X, y, model_type, splits, test_size=0.3):
    scores = []
    base_state = int(time.time())
    for i in range(splits):
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size,
                                                            random_state=base_state+i)
        model = build_model(model_type)
        model.fit(X_train, y_train)
        scores.append(model.score(X_test, y_test))

    return scores