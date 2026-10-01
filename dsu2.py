import pandas as pd

df = pd.read_csv("data.csv")

previous_grade = df["previous_grade"].where(df["previous_grade"] > 0)
improvement = (df["final_exam_score"] - previous_grade) / previous_grade * 100.
students = df[improvement.round(10).between(20, 30, inclusive="both")]
count = len(students)
job_percentage = students["part_time_job"].eq("Yes").mean() * 100

print(f"{count:.1f}")
if count:
    print(f"{job_percentage:.1f}%")
else:
    print("N/A")
