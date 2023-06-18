import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("nieruchomosci15.csv",sep=";",names=["1", "2", "3", "4", "5", "6", "7", "8"])
new_data = data.transpose().reset_index()
new_data.columns = [ "Numer","rynek", "powierzchnia", "Rok", "Wartosc"]
print(new_data)
pierwotny = new_data[new_data["rynek"] == "rynek pierwotny"]
wtorny = new_data[new_data["rynek"] == "rynek wtórny"]

fig,ax = plt.subplots(nrows=2)
explodes = [0.1,0.1,0.1,0.1]
colors=["lightblue","yellow","lime","violet"]
ax[0].pie([float(".".join(i.split())) for i in pierwotny["Wartosc"]],
          colors=colors,
          labels= pierwotny["powierzchnia"],
          shadow=True,
          explode=explodes,
          autopct="%1.2f%%")
ax[0].set_title("(góra - rynek pierwotny")
ax[1].pie([float(".".join(i.split())) for i in wtorny["Wartosc"]],colors=colors,
          labels= wtorny["powierzchnia"],shadow=True,explode=explodes,autopct="%1.2f%%")
ax[1].set_title("dół - rynek wtórny")
plt.savefig("Task5.png")
plt.show()
print([int("".join(i.split())) for i in pierwotny["Wartosc"]])