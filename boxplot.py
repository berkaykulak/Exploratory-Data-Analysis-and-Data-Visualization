import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()

print(df.describe().T)
print(df["sex"].value_counts())
print(df["smoker"].value_counts())
print(df["day"].value_counts())
print(df["time"].value_counts())

sns.boxplot(x = df["total_bill"])
sns.boxplot(x = df["total_bill"], orient = "v")
sns.boxplot(x = "day", y = "total_bill", data = df)
sns.boxplot(x = "time", y = "total_bill", data = df);
sns.boxplot(x = "size", y = "total_bill", data = df);
sns.boxplot(x = "day", y = "total_bill", hue = "sex", data = df);