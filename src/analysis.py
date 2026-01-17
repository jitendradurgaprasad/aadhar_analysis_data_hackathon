import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# -------------------------------
# Folder paths
# -------------------------------

DATA_FOLDER = "../data/aadhar_enrolment_data"
OUTPUT_FOLDER = "../outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -------------------------------
# Locate CSV files
# -------------------------------

csv_files = glob.glob(os.path.join(DATA_FOLDER, "*.csv"))

print("Looking for CSVs in:", os.path.abspath(DATA_FOLDER))
print("CSV files found:")
for file in csv_files:
    print(" -", file)

if not csv_files:
    raise FileNotFoundError("No CSV files found in the data folder.")

# -------------------------------
# Load & combine datasets
# -------------------------------

df_list = [pd.read_csv(file) for file in csv_files]
df = pd.concat(df_list, ignore_index=True)

print("\nCombined Dataset Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nSample rows:\n", df.head())

# -------------------------------
# Data cleaning
# -------------------------------

df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")
df.fillna(0, inplace=True)

df["total_enrolments"] = (
    df["age_0_5"] +
    df["age_5_17"] +
    df["age_18_greater"]
)

# -------------------------------
# Analysis 1: Age group distribution
# -------------------------------

age_data = {
    "0–5 Years": df["age_0_5"].sum(),
    "5–17 Years": df["age_5_17"].sum(),
    "18+ Years": df["age_18_greater"].sum()
}

age_df = pd.DataFrame(age_data.items(), columns=["Age Group", "Enrolments"])

plt.figure(figsize=(8, 5))
sns.barplot(x="Age Group", y="Enrolments", data=age_df)
plt.title("Aadhaar Enrolments by Age Group")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_FOLDER, "enrolments_by_age.png"))
plt.close()

# -------------------------------
# Analysis 2: Top 10 states
# -------------------------------

state_summary = (
    df.groupby("state")["total_enrolments"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
state_summary.plot(kind="bar")
plt.title("Top 10 States by Aadhaar Enrolments")
plt.xlabel("State")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_FOLDER, "top_states.png"))
plt.close()

# -------------------------------
# Analysis 3: Time trend
# -------------------------------

time_trend = df.groupby("date")["total_enrolments"].sum()

plt.figure(figsize=(12, 6))
time_trend.plot()
plt.title("Aadhaar Enrolment Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_FOLDER, "enrolment_trend.png"))
plt.close()

# -------------------------------
# Done
# -------------------------------

print("\nAnalysis complete.")
print("Graphs saved in the outputs folder.")
