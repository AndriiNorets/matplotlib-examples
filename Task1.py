import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('WineQuality.csv',sep=";")
quality_of_wine = data.groupby("quality").size()
colors = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'pink']

plt.bar(quality_of_wine.index,quality_of_wine,color=colors,edgecolor='black',label=quality_of_wine)
plt.xlabel("Quality")
plt.ylabel("Count of wine")
plt.title("Amount for each wine quality ")
plt.legend()
plt.savefig("Task1.png")
plt.show()
