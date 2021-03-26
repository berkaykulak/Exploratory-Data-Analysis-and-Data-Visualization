import seaborn as sns
fmri = sns.load_dataset("fmri")
df = fmri.copy()


sns.lineplot(x = "timepoint", y = "signal", data = df)
sns.lineplot(x = "timepoint", y = "signal", hue = "event", data = df)
sns.lineplot(x = "timepoint", y = "signal", hue = "event", style = "event", data = df);
sns.lineplot(x = "timepoint",
             y = "signal",
             hue = "event",
             style = "event",
             markers = True,  dashes = False, data = df);

sns.lineplot(x = "timepoint",
             y = "signal",
             hue = "region",
             style = "event",
             data = df);




