from random_walk import RandomWalk

import matplotlib.pyplot as plt
while True:
    plt.style.use('dark_background')
    # TIY 15-3
    rw = RandomWalk(5_000)
    rw.fill_walk()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(rw.x_values,rw.y_values,linewidth = 5)
    points = range(rw.n_points)
    # ax.scatter(rw.x_values, rw.y_values,c=points,s=1,cmap=plt.cm.Reds,edgecolors="none")
    # ax.scatter(rw.x_values[0],rw.y_values[0],c='green',s=5)
    # ax.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',s=5)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.show()
    keep_running = input("press 'n' to exit")
    if keep_running == 'n':
        break