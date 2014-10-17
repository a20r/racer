
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import racer
import racer.model as rm
import time


class LiveUncertaintyTests(unittest.TestCase):

    def setUp(self):
        self.fig = plt.figure("Uncertainty Map")
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("X Location")
        self.ax.set_ylabel("Y Location")
        self.x_step = 1.5
        self.y_step = 1.5
        self.x_min = 0
        self.y_min = 0
        self.x_max = 50
        self.y_max = 50
        self.x = np.arange(self.x_min, self.x_max, self.x_step)
        self.y = np.arange(self.y_min, self.y_max, self.y_step)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        plt.ion()
        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.y_max)
        self.ag = racer.Agent(
            rm.SinModel(10, 2, 1, 25), rm.SinModel(10, 1, 1, 25)
        )

        self.num_iter = 1000
        self.how_far = 1

        self.start_time = time.time()

    def get_zs(self):
        zs = np.array(
            [
                self.cdf(x_i, y_i)
                for x_i, y_i in zip(np.ravel(self.X), np.ravel(self.Y))
            ]
        )
        return zs

    def update(self):
        try:
            self.graph.remove()
        except:
            pass

        zs = self.get_zs()
        Z = zs.reshape(self.X.shape)
        self.graph = self.ax.pcolormesh(self.X, self.Y, Z,
                                        cmap=cm.jet, shading='gouraud')
        plt.draw()
        plt.pause(0.0001)

    def test_normal(self):
        time_step = 0.2
        t = 0
        for i in xrange(self.num_iter):
            try:
                self.cdf = lambda x, y: self.ag.get_probability(
                    x, y, t, t + self.how_far
                )
                t += time_step
                self.update()

            except Exception as e:
                print e


if __name__ == "__main__":
    unittest.main()
