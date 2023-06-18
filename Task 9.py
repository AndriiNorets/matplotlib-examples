import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("kurs14.csv",sep=";")
x_value = [int(i) for i in data["Dzień"]]
y_value = [float(".".join(i.split(","))) for i in data["Kurs CZK"]]

plt.plot(x_value,y_value,marker="d" ,label = "Kurs CZK",color="violet")
plt.xlabel("Dzień")
plt.ylabel("Kurs")
plt.legend()
plt.grid()
plt.title("Kurs CZK za 30 dni")
plt.savefig("Task9.jpg")
plt.show()





