import joblib
import pandas as pd
from pathlib import Path



class DisasterPredictor:
    def __init__(self):
        root= Path(__file__).resolve().parents[2]
        model_dir=root/"model_weights"
        self.model=joblib.load(model_dir/"disaster_relief_optimizer.pkl")
        self.disaster_type_encoder=joblib.load(model_dir/"disaster_type_encoder.pkl")
        self.target_label_encoder=joblib.load(model_dir/"label_encoder.pkl")

    def preprocess(self,data:dict):

        disaster_type=self.disaster_type_encoder.transform([data["disaster_type"]])[0]
        return pd.DataFrame({
            "disaster_type": [disaster_type],
            "affected_rate": [data["affected_rate"]],
            "homeless_rate": [data["homeless_rate"]],
            "casualty_rate": [data["casualty_rate"]],
            "damage_rate": [data["damage_rate"]],
            "duration": [data["duration"]]
            })
            

            
    def predict(self,data:dict):

        X=self.preprocess(data)
        prediction =self.model.predict(X)[0]
        probabilities=self.model.predict_proba(X)[0]
        priority=self.target_label_encoder.inverse_transform([prediction])[0]

        return{
            "relief_priority": priority,
            "probability": float(probabilities[prediction]),
            "probabilities": {label: float(prob)
                for label, prob in zip(
                    self.target_label_encoder.classes_,
                    probabilities
                )
            }
        }
