import seaborn as sns
import pandas as pd

planets = sns.load_dataset("planets")
planets.head()
df = planets.copy()

print(df.head())
print(df.tail())
print(df.info())
print(df.dtypes)



df.method = pd.Categorical(df.method)
print(df.dtypes)
print(df.head())










