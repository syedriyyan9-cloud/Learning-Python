from random_walk import RandomWalk

import matplotlib.pyplot as plt
while True:
    plt.style.use('dark_background')
    rw = RandomWalk()
    rw.fill_walk()
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values,c=rw.y_values,s=15,cmap=plt.cm.Reds)
    plt.show()
    keep_running = input("press 'n' to exit")
    if keep_running == 'n':
        break