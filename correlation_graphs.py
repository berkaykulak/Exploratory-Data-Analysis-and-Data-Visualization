import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()


sns.scatterplot(x = "total_bill", y = "tip", data = df);
sns.scatterplot(x = "total_bill", y = "tip", hue = "time",data = df);
sns.scatterplot(x = "total_bill", y = "tip", hue = "time", style = "time", data = df)
sns.scatterplot(x = "total_bill", y = "tip", hue = "day", style = "day", data = df)
sns.scatterplot(x = "total_bill", y = "tip", hue= "size", size = "size", data = df);





