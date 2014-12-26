
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import racer
import racer.model as rm
import time


class LiveUncertaintyTests(object):

    def __init__(self):
        self.fig = plt.figure("Uncertainty Map")
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("X Location")
        self.ax.set_ylabel("Y Location")
        self.x_step = 0.05
        self.y_step = 0.05
        self.x_min = -1
        self.y_min = 0
        self.x_max = 5
        self.y_max = 4
        self.x = np.arange(self.x_min, self.x_max, self.x_step)
        self.y = np.arange(self.y_min, self.y_max, self.y_step)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        plt.ion()
        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.y_max)
        self.ag = racer.Agent(
            rm.SinModel(2, 2, 1, 2), rm.LinearModel(0, 1)
        )
        self.ag_2 = racer.Agent(
            rm.SinModel(-2, 2, 1, 2), rm.LinearModel(0, 3)
        )

        self.num_iter = 1000
        self.how_far = 1

        self.start_time = time.time()
        self.start = racer.Point(25, 0)
        self.goal = racer.Point(25, 50)

    def get_zs(self):
        x_y_zipped = zip(np.ravel(self.X), np.ravel(self.Y))
        zs = np.array([self.pdf(x_i, y_i) for x_i, y_i in x_y_zipped])
        return zs

    def update(self):
        try:
            self.graph.remove()
        except:
            pass

        zs = self.get_zs()
        Z = zs.reshape(self.X.shape)
        self.graph = self.ax.pcolormesh(self.X, self.Y, Z, cmap=cm.jet)
        plt.draw()
        plt.pause(0.0000001)

    def run(self):
        time_step = 0.2
        t = 0
        for i in xrange(self.num_iter):
            self.pdf = racer.get_pdf(t, t + self.how_far, self.ag, self.ag_2)
            t += time_step
            self.update()


if __name__ == "__main__":
    lut = LiveUncertaintyTests()
    lut.run()
