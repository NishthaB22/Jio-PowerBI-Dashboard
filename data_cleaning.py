import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fix TotalCharges column
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].mean(), inplace=True)

# Add Indian telecom style regions
regions = ["North", "South", "East", "West"]
df["Region"] = np.random.choice(regions, len(df))

# Recharge category
df["RechargeCategory"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 30, 70, 120],
    labels=["Low", "Medium", "High"]
)

# Convert churn values
df["Churn"] = df["Churn"].replace({
    "Yes":"Churned",
    "No":"Active"
})

# Save cleaned file
df.to_csv("jio_cleaned_data.csv", index=False)

print("Done Successfully")