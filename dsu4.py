import pandas as pd  
import numpy as np 

df = pd.read_csv("data.csv")
df = df.dropna(subset=["study_time_hours", "final_exam_score", "previous_grade", "attendance_percent", "sleep_hours"]).copy()

slope, intercept = np.polyfit(df["study_time_hours"], df["final_exam_score"], 1)

df["expected"] = slope * df["study_time_hours"] + intercept
df["difference"] = df["final_exam_score"] - df["expected"]

print(f"{slope:.2f}")
print(f"{intercept:.2f}")

unexpected = df[df["difference"].abs() >= 10].copy()
unexpected["gap_size"] = unexpected["difference"].abs()

students = unexpected.sort_values("gap_size", ascending=False).head(3)

columns = ["student_id", "study_time_hours", "final_exam_score", "expected", "difference", "previous_grade", "attendance_percent", "sleep_hours"]
print(students[columns].to_string(index=False, header=False, float_format="{:.1f}".format))


print(f"{df['previous_grade'].corr(df['difference']):.3f}")
print(f"{df['attendance_percent'].corr(df['difference']):.3f}")
print(f"{df['sleep_hours'].corr(df['difference']):.3f}")

higher = df[df["difference"] >= 10]
close = df[df["difference"].abs() < 10]
lower = df[df["difference"] <= -10]

for group in [higher, close, lower]:  
    print(f"{len(group)} {group['previous_grade'].mean():.1f} {group['attendance_percent'].mean():.1f} {group['sleep_hours'].mean():.1f}")

