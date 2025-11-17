import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. READ YOUR EXCEL FILE
# ---------------------------
df = pd.read_excel("Book1.xlsx")

# Check structure
print("\n=== STUDENT DATA ===\n")
print(df)

# ---------------------------
# 2. CALCULATE AVERAGE PER STUDENT
# ---------------------------
df["Average"] = df.iloc[:, 2:].mean(axis=1)

print("\n=== AVERAGE SCORE PER STUDENT ===\n")
print(df[["Student_ID", "Average"]])

# ---------------------------
# 3. SUBJECT-WISE AVERAGE
# ---------------------------
subject_avg = df.iloc[:, 2:].mean()
print("\n=== SUBJECT-WISE AVERAGE ===\n")
print(subject_avg)

# ---------------------------
# 4. PERFORMANCE TREND GRAPH
# ---------------------------
plt.figure(figsize=(12, 6))

for i in range(len(df)):
    student_id = df.loc[i, "Student_ID"]
    marks = df.iloc[i, 2:-1]  # Only Test_1 to Test_12
    
    plt.plot(
        df.columns[2:-1], 
        marks, 
        marker='o', 
        linewidth=2,
        label=f"Student {student_id}"
    )

plt.title("Student Performance Trend Across 12 Tests", fontsize=16)
plt.xlabel("Tests", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ---------------------------
# 5. TOP + WEAK STUDENT
# ---------------------------
top = df.loc[df["Average"].idxmax()]
weak = df.loc[df["Average"].idxmin()]

print("\n=== TOP & WEAK STUDENT ===")
print(f"Top Performer : Student {top['Student_ID']} → Avg = {top['Average']:.2f}")
print(f"Weakest Student: Student {weak['Student_ID']} → Avg = {weak['Average']:.2f}")
