import pandas as pd

df = pd.read_csv("sample_data.csv")
print("Before Cleaning:\n", df.head())

df = df.dropna()
df.columns = [c.lower().replace(" ", "_") for c in df.columns]
df.to_csv("cleaned_data.csv", index=False)
print("✅ Cleaned data saved as cleaned_data.csv")
