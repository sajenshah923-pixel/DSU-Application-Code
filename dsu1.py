import pandas as pd
df = pd.read_csv("data.csv")

students = df[df["parental_education"] == "High School"]
count = len(students)
average_attendance = students["attendance_percent"].mean()


print(count)
print(f"{average_attendance:.1f}")