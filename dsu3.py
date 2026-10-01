import pandas as pd  

df = pd.read_csv("data.csv")

df = df[["study_time_hours", "sleep_hours", "final_exam_score"]].dropna()

study_r = df["study_time_hours"].corr(df["final_exam_score"])
sleep_r = df["sleep_hours"].corr(df["final_exam_score"])


print(f"{study_r:.3f}")
print(f"{sleep_r:.3f}")
print(f"{study_r ** 2:.3f}")
print(f"{sleep_r ** 2:.3f}")

df["study_group"] = df["study_time_hours"] // 2 * 2
df["sleep_group"] = df["sleep_hours"] // 2 * 2

groups = df.groupby(["study_group", "sleep_group"])["final_exam_score"].agg(["count", "mean"])
groups = groups[groups["count"] >= 20]
groups = groups.sort_values("mean", ascending=False)
groups = groups.reset_index()

print(groups.to_string(index=False, header=False, float_format="{:.1f}".format))
