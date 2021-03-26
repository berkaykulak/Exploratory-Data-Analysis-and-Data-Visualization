import seaborn as sns
from pandas.api.types import CategoricalDtype
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()
cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))


print(df.head())

print(sns.catplot(x = "cut", y = "price", data = df))
print(sns.barplot(x = "cut", y = "price", hue = "color", data = df))
print(df.groupby(["cut","color"])["price"].mean())



