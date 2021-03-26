import seaborn as sns
fmri = sns.load_dataset("fmri")
df = fmri.copy()

print(df.shape)
print(df["timepoint"].describe())
print(df["timepoint"].describe())
print(df["signal"].describe())
print(df.groupby("timepoint")["signal"].count())
print(df.groupby("signal").count())
print(df.groupby("timepoint")["signal"].describe())



