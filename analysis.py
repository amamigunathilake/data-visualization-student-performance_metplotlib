import pandas as pd
import matplotlib.pyplot as plt

print("✅ Script started")

# Load dataset
df = pd.read_csv("students.csv")
print("✅ CSV loaded")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

# Histogram - Marks distribution
plt.figure()
plt.hist(df["marks"])
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.show(block=True)

# Scatter plot - Attendance vs Marks
plt.figure()
plt.scatter(df["attendance"], df["marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show(block=True)

# Bar chart - Average marks by gender
avg = df.groupby("gender")["marks"].mean()

plt.figure()
avg.plot(kind="bar")
plt.title("Average Marks by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show(block=True)

print("\nLow performing students (marks < 50):")
print(df[df["marks"] < 50])

input("\nPress Enter to exit...")
