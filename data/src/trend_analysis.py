import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/dataset.csv")

print(df.head())

plt.plot(df["id"], df["value"])
plt.title("Trend Analysis")
plt.xlabel("ID")
plt.ylabel("Value")
plt.savefig("results/figures/trend_plot.png")
plt.clf()

sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.savefig("results/figures/heatmap.png")
