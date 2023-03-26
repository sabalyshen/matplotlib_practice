import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples, s=15)
    #突出起點跟終點
    plt.scatter(rw.x_values[0], rw.y_values[0], c='b', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='r', s=100)
    
    #隱藏座標軸
    plt.axis('off')
    
    plt.show()
    
    keep_running = input("Make another walk?(y/n) ")
    if keep_running =='n':
        break
