import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
data = {
    "Heart Rate (bpm)": np.random.randint(60, 100, 1000),
    "Blood Pressure (mmHg)": np.random.randint(90, 140, 1000),
    "Body Temperature (°F)": np.round(np.random.normal(98.6, 0.7, 1000), 1),
    "Oxygen Saturation (%)": np.random.randint(95, 100, 1000),
    "Step Count": np.random.randint(2000, 15000, 1000),
    "Calories Burned": np.random.randint(1500, 3000, 1000),
    "Sleep Duration (hours)": np.round(np.random.uniform(4, 9, 1000), 1),
    "Stress Level (1-10)": np.random.randint(1, 10, 1000)
}

# Create DataFrame
health_data_df = pd.DataFrame(data)

# Determine string values based on numerical columns
health_data_df["Activity Level"] = pd.cut(
    health_data_df["Step Count"],
    bins=[0, 4000, 10000, np.inf],
    labels=["Low", "Moderate", "High"]
)

health_data_df["Health Status"] = np.select(
    [
        (health_data_df["Heart Rate (bpm)"] < 70) & (health_data_df["Blood Pressure (mmHg)"] < 110),
        (health_data_df["Heart Rate (bpm)"] >= 70) & (health_data_df["Heart Rate (bpm)"] < 90) & (health_data_df["Blood Pressure (mmHg)"] < 130),
        (health_data_df["Heart Rate (bpm)"] >= 90) | (health_data_df["Blood Pressure (mmHg)"] >= 130)
    ],
    ["Excellent", "Good", "Warning"],
    default="Critical"
)

health_data_df["Sleep Quality"] = pd.cut(
    health_data_df["Sleep Duration (hours)"],
    bins=[0, 5, 7, np.inf],
    labels=["Poor", "Average", "Good"]
)

health_data_df["Stress Level Category"] = pd.cut(
    health_data_df["Stress Level (1-10)"],
    bins=[0, 3, 6, 10],
    labels=["Low", "Moderate", "High"]
)

# Save to Excel
file_path = 'health_monitoring_data.xlsx'
health_data_df.to_excel(file_path, index=False)

file_path
