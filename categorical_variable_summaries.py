import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()

print(df.head())

kat_df = df.select_dtypes(include = ["object"])
kat_df.head(5)


print(kat_df.method.unique())
print(kat_df["method"].value_counts().count())
print(kat_df["method"].value_counts())
print(df["method"].value_counts().plot.barh())












