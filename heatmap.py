import seaborn as sns
import matplotlib.pyplot as plt
flights = sns.load_dataset('flights')
df = flights.copy()

print(df.head())
print(df.shape)
print(df["passengers"].describe())
df = df.pivot("month", "year", "passengers")
print(df)

sns.heatmap(df)
sns.heatmap(df, annot = True, fmt = "d")
sns.heatmap(df, annot = True, fmt = "d", linewidths = .5)
sns.heatmap(df, annot = True, fmt = "d", linewidths = .5, cbar = False);
plt.show()








