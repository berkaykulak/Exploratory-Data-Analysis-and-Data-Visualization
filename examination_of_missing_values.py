import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()
print(df.head())

print(df.isnull().values.any())
print(df["orbital_period"].fillna(0, inplace = True))
print(df.isnull().sum())
print(df.isnull().sum())
print(df["mass"].fillna(df.mass.mean(), inplace = True))
print(df.isnull().sum())
print(df.fillna(df.mean(), inplace = True))
print(df.isnull().sum())


df = planets.copy()

print(df.head())
print(df.isnull().sum())



















