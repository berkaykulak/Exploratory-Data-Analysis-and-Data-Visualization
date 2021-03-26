import seaborn as sns
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()

print(df.head())

print(sns.distplot(df.price, kde = False))
print(df["price"].describe())
print(sns.distplot(df.price, bins = 10, kde = False))
print(sns.distplot(df.price))
print(sns.distplot(df.price, hist = False))
print(sns.kdeplot(df.price, shade = True))

print(sns.kdeplot(df.price, shade = True))
print((sns
 .FacetGrid(df,
              hue = "cut",
              height = 5,
              xlim = (0, 10000))
 .map(sns.kdeplot, "price", shade= True)
 .add_legend()
))

sns.catplot(x = "cut", y = "price", hue = "color", kind = "point", data = df);