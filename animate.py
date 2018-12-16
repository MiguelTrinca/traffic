from cars import Cars
from matplotlib import animation
import numpy as np
import osmnx as ox
import simulation as sim

dt = 1 / 1000
N = 1

# load figure for animation
G = ox.load_graphml('piedmont.graphml')
G = ox.project_graph(G)
fig, ax = ox.plot_graph(G)
ax.set_title('Piedmont, California')

# initialize empty particle points for animation
cars = sum([ax.plot([], [], 'ro', ms=3) for n in np.arange(N)], [])
state = Cars(sim.init_culdesac_start_location(N))


def init():
    """
    initializes the animation
    :return: particles, cube
    """
    for car in cars:
        car.set_data([], [])
    return cars


def animate(i):
    """
    perform animation step
    :param i:
    :return:
    """

    state.update(dt)

    for car, car_dict in zip(cars, state.state):
        x = car_dict['position'][0]
        y = car_dict['position'][1]
        car.set_data(x, y)

    fig.canvas.draw()
    return cars


# create animation object
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=30, blit=True)
# plt.show()
ani.save('traffic.html', fps=30, extra_args=['-vcodec', 'libx264'])
