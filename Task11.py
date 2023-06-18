import matplotlib.pyplot as plt

labels = ["A","B","C","D","E"]
values_1 = [35,47,15,43,41]
values_2 = [-30,-34,-40,-37,-32]
colors_1 = ["pink","lightblue","seagreen","lime","slateblue"]
colors_2 = ["violet","salmon","cornflowerblue","slategray","olive"]
fig,ax = plt.subplots(ncols=2)
ax[0].barh(labels,values_1,color=colors_1)
ax[1].barh(labels,values_2,color=colors_2)
ax[0].set_xticks([0,10,20,30,40])
ax[1].set_xticks([-30,-20,-10,0])
ax[0].set_title("Left graphic")
ax[1].set_title("Right graphic")
plt.savefig("Task11.jpg")
plt.show()




