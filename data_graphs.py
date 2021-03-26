import seaborn as sns
from pandas.api.types import CategoricalDtype
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()

print(df.info())
print(df.describe().T)
print(df.head())
print(df["cut"].value_counts())
print(df["color"].value_counts())
print(df.cut.head())
df.cut = df.cut.astype(CategoricalDtype(ordered = True))
print(df.dtypes)
print(df.cut.head(1))
cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))
print(df.cut.head(1))
print(df["cut"].value_counts().plot.barh().set_title("Cut Değişkeninin Sınıf Frekansları"))



print((df["cut"]
 .value_counts()
 .plot.barh()
 .set_title("Cut Değişkeninin Sınıf Frekansları")))
print(sns.barplot(x = "cut", y = df.cut.index, data= df))
print()