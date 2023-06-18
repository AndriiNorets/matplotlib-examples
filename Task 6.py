import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("samochodyosobowe11.csv",sep=";")
new_data = data.transpose().reset_index()
new_data.columns = [ "pojemnosc silnika", "Rok", "ille", "Wartosc"]
data_2018 =  new_data[new_data["Rok"] == "2018"]
data_2019 = new_data[new_data["Rok"] == "2019"]

fig,ax = plt.subplots(ncols=2)
explodes = [0.05,0.05,0.05]
ax[0].pie(data_2018["Wartosc"],autopct="%1.2f%%",labels=data_2018["pojemnosc silnika"],
          colors=["red","lightpink","lightblue"],shadow=True,explode=explodes)
ax[1].pie(data_2019["Wartosc"],autopct="%1.2f%%",labels=data_2019["pojemnosc silnika"],
          colors=["yellow","orange","lightgreen"],shadow=True,explode=explodes)
ax[0].set_title("2018")
ax[1].set_title("2019")
plt.savefig("Task6.pdf")
plt.show()
