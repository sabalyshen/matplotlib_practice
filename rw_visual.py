import matplotlib.pyplot as plt

from random_walk import RandomWalk
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Purples, s=15)
plt.show()