from pathlib import Path
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np

# =====================================================
# Paths
# =====================================================

ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = ROOT / "models" / "disaster_relief_optimization.pkl"
DISASTER_ENCODER_PATH = ROOT / "models" / "disaster_type_encoder.pkl"
TARGET_ENCODER_PATH = ROOT / "models" / "label_encoder.pkl"
DATA_PATH = ROOT / "data" / "preprocessed" / "preprocessed_dataset.csv"

# =====================================================
# Features used during training
# =====================================================

FEATURES = [
    "disaster_type",
    "affected_rate",
    "homeless_rate",
    "casualty_rate",
    "damage_rate",
    "duration"
]

# =====================================================
# Helper Functions
# =====================================================

def load_model():
    return joblib.load(MODEL_PATH)



def load_disaster_encoder():
    return joblib.load(DISASTER_ENCODER_PATH)


def load_target_encoder():
    return joblib.load(TARGET_ENCODER_PATH)


def load_df():
    df = pd.read_csv(DATA_PATH)
    encoder = load_disaster_encoder()
    df["disaster_type"] = encoder.transform(df["disaster_type"])

    return df


# =====================================================
# Tests
# =====================================================

def test_model_exists():
    assert MODEL_PATH.exists()


def test_model_load():
    assert load_model() is not None


def test_prediction_shape():

    model = load_model()
    df = load_df()

    X = df[FEATURES]
    preds = model.predict(X.head(10))
    
    assert len(preds) == 10


def test_prediction_classes():

    model = load_model()
    df = load_df()

    X = df[FEATURES]

    preds = model.predict(X.head(20))

    assert set(preds).issubset({0, 1, 2})


def test_prediction_probabilities():

    model = load_model()
    df = load_df()

    X = df[FEATURES]

    probs = model.predict_proba(X.head(5))

    assert probs.shape == (5, 3)


def test_probability_sum():

    model = load_model()
    df = load_df()

    X = df[FEATURES]

    probs = model.predict_proba(X.head(5))

    assert np.allclose(probs.sum(axis=1), 1.0)


def test_model_accuracy():

    model = load_model()
    df = load_df()
    target_encoder=load_target_encoder()

    X = df[FEATURES]
    y = target_encoder.transform(df["relief_priority"])

    preds = model.predict(X)

    accuracy = accuracy_score(y, preds)

    assert accuracy >= 0.90, f"Accuracy dropped to {accuracy:.2%}"


# =====================================================
# Run Tests
# =====================================================

if __name__ == "__main__":

    test_model_exists()
    test_model_load()
    test_prediction_shape()
    test_prediction_classes()
    test_prediction_probabilities()
    test_probability_sum()
    test_model_accuracy()

    print("✅ All model tests passed!")