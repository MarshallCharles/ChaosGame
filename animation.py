import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random as rand
import time
import random_numbers as chaos
import os
style.use('fivethirtyeight')

verbose = False
#bounds = [(0,0),(1,0),(.5,1)]
#bounds = [(.2,0),(.8,0),(.5,1),(0,.6),(1,.6)]
bounds = [(.5,0),(.5,1),(1,.3),(0,.3),(1,.7),(0,.7)]
# current = [.2,0]
# current = [0,0]
current = [.5,0]
options = []
for i in range(len(bounds)):
    options.append(i)

class Animated_Scat:
    def __init__(self):

        self.stream = self.data_stream()
         # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=1,
                                          init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        x, y= 0,0
        self.scat = self.ax.scatter(x, y, c = 'black')
        self.ax.axis([0, 1, 0, 1])
        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def data_stream(self):
        global current, bounds

        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect."""
        stream = [[0],[0]]
        iter = 0
        cur = current
        while True:
            cur,iter = chaos.random_numbers(options,bounds, iter, cur)
            stream[0].append(cur[0])
            stream[1].append(cur[1])
            yield np.c_[stream[0],stream[1]]

    def update(self, i):
        """Update the scatter plot."""
        data = next(self.stream)
        # Set x and y data...
        self.scat.set_offsets(data[:, :2])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,


if __name__ == '__main__':
    a = Animated_Scat()
    plt.show()




#

# fig = plt.figure()
# ax = plt.axes(xlim = (0,1),ylim = (0,1))
# scat = ax.plot([0],[0])
#
# bounds = [(0,0),(1,0),(.5,1)]
# options = []
# for i in range(len(bounds)):
#     options.append(i)
#
#
# def init():
#     scat.set_data([0],[0])
#     return points,
# def animate(i):
#     iter = 0
#     cur = 0,0
#     cur, iter = chaos.random_numbers(options,iter,cur)
#     scat.set_data (cur[0],cur[1])
#     return points
#
# def main():
#
#     ani = animation.FuncAnimation(fig,animate,init_func = init,frames=200, interval = 1000,blit=True)
#     plt.show()
#
# if __name__=='__main__':
#     main()
