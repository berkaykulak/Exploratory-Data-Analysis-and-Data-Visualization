import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()

sns.catplot(y = "total_bill", kind = "violin", data = df)

sns.catplot(x= "day", y = "total_bill", kind = "violin", data = df);
sns.catplot(x= "day", y = "total_bill", hue = "sex",kind = "violin", data = df);



