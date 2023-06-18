import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile('przewozy24.xlsx')
data = pd.read_excel(xls)
melted_data = pd.melt(data,id_vars="Nazwa",var_name='Rok', value_name='Wartosc')
slaskie = melted_data[melted_data["Nazwa"] == "ŚLĄSKIE"]
mazowieckie = melted_data[melted_data["Nazwa"] == "MAZOWIECKIE"]

fig,ax = plt.subplots(ncols=2)
labels = [2014,2015,2016,2017]
colors = ["orange","violet","papayawhip","cyan"]
ax[0].bar(labels,slaskie["Wartosc"],color=colors,edgecolor='indigo',label=slaskie["Wartosc"])
ax[1].bar(labels,mazowieckie["Wartosc"],color=colors,edgecolor='indigo',label=mazowieckie["Wartosc"])
ax[0].set_title("ŚLĄSKIE")
ax[1].set_title("MAZOWIECKIE")
ax[0].set_xticks(labels)
ax[1].set_xticks(labels)
ax[0].legend()
ax[1].legend()
ax[0].set_xlabel("Rok")
ax[0].set_ylabel("Liczba przewozów")
ax[1].set_xlabel("Rok")
ax[1].set_ylabel("Liczba przewozów")
plt.savefig("Task7.jpg")
plt.show()


