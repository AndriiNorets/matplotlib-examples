import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('WineQuality.csv',sep=";")

color = data["pH"]
plt.scatter(x=data["volatile acidity"],y=data["pH"],s=20,c=color)
plt.xlabel("volatile acidity")
plt.ylabel("pH")
plt.title("The relationship between volatile acidity and pH.")
plt.colorbar()
plt.savefig("Task2.jpg")
plt.show()
