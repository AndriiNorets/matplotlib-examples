import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hotele32.csv",sep="#")
melted_data = pd.melt(data,id_vars='Nazwa',var_name="Rok",value_name="Wartosc")
w_1 = melted_data[melted_data["Nazwa"] == 'ZACHODNIOPOMORSKIE']
w_2 = melted_data[melted_data["Nazwa"] == 'WIELKOPOLSKIE']
w_3 = melted_data[melted_data["Nazwa"] == 'LUBUSKIE']
w_4 = melted_data[melted_data["Nazwa"] == 'ŚWIĘTOKRZYSKIE']
w_5 = melted_data[melted_data["Nazwa"] == 'ŚLĄSKIE']
area = 100
plt.scatter(w_1["Rok"],w_1["Wartosc"],s=area,marker="x",label="ZACHODNIOPOMORSKIE")
plt.scatter(w_2["Rok"],w_2["Wartosc"],s=area,marker="d",label="WIELKOPOLSKIE")
plt.scatter(w_3["Rok"],w_3["Wartosc"],s=area,marker=">",label="LUBUSKIE")
plt.scatter(w_4["Rok"],w_4["Wartosc"],s=area,marker="s",label="ŚWIĘTOKRZYSKIE")
plt.scatter(w_5["Rok"],w_5["Wartosc"],s=area,marker="p",label="ŚLĄSKIE")
plt.grid()
plt.legend()
plt.xlabel("Rok")
plt.ylabel("Liczba hoteli")
plt.title("Liczba hoteli w poszczególnych województwach")
plt.savefig("Task8.png")
plt.show()
