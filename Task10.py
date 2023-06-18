import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("studenci17.csv",sep=";")
data = data[data["Tryby nauczania"] == "studia stacjonarne (dzienne)"]
m_2016 = data[(data["Rok"] == 2016) & (data["Płeć"] == "mężczyźni")]
m_2017 = data[(data["Rok"] == 2017) & (data["Płeć"] == "mężczyźni")]
k_2016 = data[(data["Rok"] == 2016) & (data["Płeć"] == "kobiety")]
k_2017 = data[(data["Rok"] == 2017) & (data["Płeć"] == "kobiety")]

fig,ax = plt.subplots(ncols=2)
categories = ["mężczyźni","kobiety"]
colors = ["lightblue","pink"]
values = [m_2016["Wartosc"].max(),k_2016["Wartosc"].max()]
values_2 = [m_2017["Wartosc"].max(),k_2017["Wartosc"].max()]
ax[0].bar(categories, values,color=colors,label=values)
ax[1].bar(categories, values_2,color=colors,label=values_2)
ax[0].set_title("Dane za 2016 rok")
ax[1].set_title("Dane za 2017 rok")
ax[0].legend()
ax[1].legend()
plt.savefig("Task10.png")
plt.show()


