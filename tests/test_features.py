import pandas as pd

df=pd.read_csv("../data/preprocessed/preprocessed_dataset.csv")

# Veriftying the engineered feature was successfully created
def test_engineered_columns_exist():
    
    expected_columns = [
        "affected_rate",
        "homeless_rate",
        "casualty_rate",
        "damage_rate",
        "duration",
        "priority_score",
        "relief_priority"
    ]
    for column in expected_columns:
        assert column in df.columns

# Test for missing values

def test_number_missing_values():
    
     columns = [
        "affected_rate",
        "homeless_rate",
        "casualty_rate",
        "damage_rate",
        "duration"
    ]
     
     for col in columns:
         assert df[col].isna().sum()==0

# Test that Rates are non-negative values:

def test_rates_none_negative():
    columns = [
        "affected_rate",
        "homeless_rate",
        "casualty_rate",
        "damage_rate"
    ]
    for col in columns:
        assert(df[col]>=0).all()

# Test elief Priority:
def test_relief_priority():
    expected={"Low", "Medium", "High"}
    assert set(df["relief_priority"].unique())==expected

# Test priority score

def test_priority_score():
    assert df["priority_score"].between(0,1).all()


if __name__=="__main__":
    test_engineered_columns_exist()
    test_number_missing_values()
    test_rates_none_negative()
    test_relief_priority()
    test_priority_score()
    print("All feature engineered pass!")






