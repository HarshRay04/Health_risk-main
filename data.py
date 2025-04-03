import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of samples
n = 3000

# Generate synthetic data
data = {
    # Health metrics with realistic ranges
    "BMI": np.clip(np.random.normal(25, 5, n), 18, 40),  # Mean 25, Std 5, Clipped between 18 and 40
    "Heart Rate": np.random.randint(50, 120, n),
    "Blood Pressure": [f"{np.random.randint(90, 160)}/{np.random.randint(60, 100)}" for _ in range(n)],
    "Oxygen Saturation": np.random.randint(90, 100, n),
    "Respiratory Rate": np.random.randint(12, 25, n),
    "Blood Sugar Level": np.random.randint(70, 200, n),
    "Cholesterol Level": np.random.randint(100, 300, n),
    
    # Lifestyle factors (Yes/No for Exercises and Diet)
    "Exercises": np.random.choice(["Yes", "No"], n, p=[0.4, 0.6]),
    "Follows Diet": np.random.choice(["Yes", "No"], n, p=[0.3, 0.7]),
    "Sleep Quality": np.random.choice(["Good", "Poor"], n, p=[0.5, 0.5]),
}

# Create DataFrame
df = pd.DataFrame(data)

# Assign Risk Level based on conditions
def assign_risk_level(row):
    # Extract systolic BP (first value in "Blood Pressure")
    systolic_bp = int(row["Blood Pressure"].split("/")[0])
    
    # Conditions for High Risk
    if (
        row["BMI"] >= 30
        or systolic_bp >= 140
        or row["Blood Sugar Level"] >= 180
        or row["Cholesterol Level"] >= 240
        or (row["Sleep Quality"] == "Poor" and row["Exercises"] == "No" and row["Follows Diet"] == "No")
    ):
        return "High"
    
    # Conditions for Medium Risk
    elif (
        (25 <= row["BMI"] < 30)
        or (120 <= systolic_bp < 140)
        or (140 <= row["Blood Sugar Level"] < 180)
        or (200 <= row["Cholesterol Level"] < 240)
        or (row["Exercises"] == "Yes" and row["Follows Diet"] == "No")
    ):
        return "Medium"
    
    # Default to Low Risk
    else:
        return "Low"

df["Risk Level"] = df.apply(assign_risk_level, axis=1)

# Save to CSV
df.to_csv("health_risk_dataset.csv", index=False)