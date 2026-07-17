from pathlib import Path
import joblib
import pandas as pd


# ===================================================
# PATHS
#====================================================
ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = ROOT / "data" / "preprocessed" / "preprocessed_dataset.csv"
DISASTER_ENCODER_PATH = ROOT / "models" / "disaster_type_encoder.pkl"

# ==================================================
# FEATURES USED DURING IN TRAINING
# ==================================================
FEATURES = [
    "disaster_type",
    "affected_rate",
    "homeless_rate",
    "casualty_rate",
    "damage_rate",
    "duration",
    "priority_score",
    "relief_priority"
]
NUMERIC_FEATURES = [
    "affected_rate",
    "homeless_rate",
    "casualty_rate",
    "damage_rate",
    "duration",
    "priority_score"
]

# ==================================================
# HELPER FUNCTIONS
# ==================================================
def load_df():
    return pd.read_csv(DATA_PATH)


def load_encoder():
    return joblib.load(DISASTER_ENCODER_PATH)

# ===================================================
# TESTS
# ===================================================

def test_dataset_exists():
    assert DATA_PATH.exists()

def test_dataset_loads():
    df = load_df()
    assert not df.empty

def test_required_columns():
    df = load_df()
    for col in FEATURES:
        assert col in df.columns

def test_no_missing_values():
    df = load_df()
    assert df[FEATURES].isnull().sum().sum() == 0

def test_no_duplicates():
    df = load_df()
    assert df.duplicated().sum() == 0

def test_disaster_encoder():
    df = load_df()
    encoder = load_encoder()
    encoded = encoder.transform(df["disaster_type"])
    assert len(encoded) == len(df)

def test_encoded_values():
    df = load_df()
    encoder = load_encoder()
    encoded = encoder.transform(df["disaster_type"])
    assert encoded.min() >= 0


def test_numeric_columns():
    df = load_df()
    for col in NUMERIC_FEATURES:
        assert pd.api.types.is_numeric_dtype(df[col])

def test_target_labels():
    df = load_df()
    expected = {"Low", "Medium", "High"}
    assert set(df["relief_priority"].unique()) == expected

# ===================================================
# RUN TESTS
# ===================================================

if __name__ == "__main__":

    test_dataset_exists()
    test_dataset_loads()
    test_required_columns()
    test_no_missing_values()
    test_no_duplicates()
    test_disaster_encoder()
    test_encoded_values()
    test_numeric_columns()
    test_target_labels()

    print("✅ All preprocessing tests passed!")
    