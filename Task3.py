import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('WineQuality.csv',sep=";")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = data["pH"]
scatter = ax.scatter(data["residual sugar"], data["pH"], data["alcohol"], c=colors)
ax.set_xlabel("Residual Sugar")
ax.set_ylabel("pH")
ax.set_zlabel("Alcohol")
plt.colorbar(scatter)
plt.title("Content pH between alcohol and residual sugar")
plt.show()
