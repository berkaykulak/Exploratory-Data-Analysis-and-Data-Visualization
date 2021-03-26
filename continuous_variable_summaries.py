import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()

print(df.head())

df_num = df.select_dtypes(include = ["float64", "int64"])
print(df_num.head())
print(df_num.describe().T)
print(df_num["distance"].describe())
print("Ortalama: " + str(df_num["distance"].mean()))
print("Dolu Gözlem Sayısı: " + str(df_num["distance"].count()))
print("Maksimum Değer: " + str(df_num["distance"].max()))
print("Minimum Değer: " + str(df_num["distance"].min()))
print("Medyan: " + str(df_num["distance"].median()))
print("Standart Sapma: " + str(df_num["distance"].std()))














