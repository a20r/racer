

# because stupid pylint
__all__ = ["Axes3D"]

import networkx as nx
import matplotlib
# matplotlib.use('module://mplh5canvas.backend_h5canvas')
# import mplh5canvas
# import matplotlib.pyplot as plt
import pylab as plt
import warnings
from mpl_toolkits.mplot3d import Axes3D


class STRoadmapDrawer(object):

    def __init__(self, rm):
        warnings.filterwarnings("ignore")
        self.rm = rm
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")

    def clear(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        return self

    def get_xs_ys_ts(self, node_list):
        xs = list()
        ys = list()
        ts = list()
        for stp in node_list:
            xs.append(stp.x)
            ys.append(stp.y)
            ts.append(stp.t)

        return xs, ys, ts

    def draw_nodes(self):
        xs, ys, ts = self.get_xs_ys_ts(self.rm.nodes())
        self.ax.scatter(xs, ys, ts, alpha=0.5)

    def draw_path(self, path):
        xs, ys, ts = self.get_xs_ys_ts(path)
        for i, s_n in enumerate(path[:-1]):
            e_n = path[i + 1]
            self.ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y], [s_n.t, e_n.t],
                         "r", linewidth=2)

    def draw_agent(self, ag, t_m):
        num_samples = 20
        t_step = t_m / num_samples
        xs = list()
        ys = list()
        ts = list()
        for i in xrange(num_samples):
            t = i * t_step
            ag_pt = ag.get_position(t)
            xs.append(ag_pt.x)
            ys.append(ag_pt.y)
            ts.append(t)

        self.ax.plot(xs, ys, ts, "y", linewidth=2)

    def show(self):
        self.ax.set_xlabel("X [meters]")
        self.ax.set_ylabel("Y [meters]")
        self.ax.set_zlabel("Time [seconds]")
        plt.show()


def make(rm):
    return STRoadmapDrawer(rm)
