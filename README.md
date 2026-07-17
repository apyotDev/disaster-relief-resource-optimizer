---

# 📊 Results & Model Evaluation

The XGBoost model was evaluated using multiple performance metrics and visualization techniques to ensure reliable disaster relief priority classification.

## 🎯 Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | **97.98%** |
| Precision | **97.98%** |
| Recall | **97.98%** |
| F1 Score | **97.98%** |

> *The model demonstrates excellent classification performance across all three relief priority classes.*

---

## 🔥 Confusion Matrix

The confusion matrix illustrates the classification performance of the model by comparing predicted and actual relief priority classes.

<p align="center">
    <img src="reports/confusion_matrix.png" width="700">
</p>

**Observations**

- High Priority incidents were classified with very high accuracy.
- Low Priority incidents achieved perfect prediction in most cases.
- Only a few Medium Priority incidents were misclassified.
- Overall, the model shows excellent class separation with minimal prediction errors.

---

## 📈 Feature Importance

Feature importance identifies which disaster indicators contribute the most to relief priority prediction.

<p align="center">
    <img src="reports/feature_importance.png" width="700">
</p>

### Key Findings

| Rank | Feature | Importance |
|------|---------|-----------:|
| 1 | affected_rate | ⭐ Highest |
| 2 | damage_rate | High |
| 3 | duration | Moderate |
| 4 | homeless_rate | Moderate |
| 5 | disaster_type | Low |
| 6 | casualty_rate | Lowest |

The model primarily relies on the proportion of affected individuals and infrastructure damage when determining disaster relief priority.

---

## 📊 Correlation Heatmap

The correlation heatmap illustrates relationships among disaster-related variables used during model training.

<p align="center">
    <img src="reports/correlation_heatmap.png" width="700">
</p>

### Observations

- **Affected Rate** has a strong positive correlation with **Damage Rate** (**0.76**).
- **Duration** is positively correlated with **Casualty Rate** (**0.73**).
- **Homeless Rate** moderately correlates with **Damage Rate** (**0.53**).
- Most remaining features show weak correlations, indicating they contribute unique information to the prediction model.

---

## 📌 Model Insights

The trained XGBoost classifier learned that disaster relief priority is primarily influenced by:

- Population affected
- Infrastructure damage
- Disaster duration
- Number of displaced residents
- Disaster type
- Casualty rate

These findings align with real-world disaster response strategies where highly affected populations and severe infrastructure damage typically require immediate resource allocation.

---
