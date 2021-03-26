import seaborn as sns;
iris = sns.load_dataset("iris")
df = iris.copy()

print(df.head())
print(df.dtypes)
print(df.shape)

sns.pairplot(df)

sns.pairplot(df, hue = "species")
sns.pairplot(df, hue = "species", markers = ["o","s","D"])
sns.pairplot(df, kind = "reg", hue = "species")