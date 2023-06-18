import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('WineQuality.csv',sep=";")
red = data[data["type"] == "red"]
white = data[data["type"] == "white"]

plt.bar(x=[1],width=0.5,height=red["alcohol"].mean(),color="red",label="red wine")
plt.bar(x=[2],width=0.5,height=white["alcohol"].mean(),color="pink",label="white wine")
plt.xticks(ticks=[1, 2],labels=[str(round(red["alcohol"].mean(),2))+"%" ,
                                str(round(white["alcohol"].mean(),2))+"%" ])
plt.title("Average value of alcohol in red and white wines")
plt.legend()
plt.savefig("Task4.png")
plt.show()
