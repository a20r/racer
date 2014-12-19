

# because stupid pylint
__all__ = ["Axes3D"]

import networkx as nx
import matplotlib.pyplot as plt
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

    def draw_graph(self):
        """
        Beware: For large graphs, this would take a while
        Also, doesnt work yet...
        """
        for s_n, e_ns in self.rm.get_graph().iteritems():
            for e_n in e_ns:
                self.ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y], [s_n.t, e_n.t])

    def draw_path(self, path):
        xs, ys, ts = self.get_xs_ys_ts(path)
        for i, s_n in enumerate(path[:-1]):
            e_n = path[i + 1]
            self.ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y], [s_n.t, e_n.t],
                         linewidth=2)

    def show(self):
        self.ax.set_xlabel("X [meters]")
        self.ax.set_ylabel("Y [meters]")
        self.ax.set_zlabel("Time [seconds]")
        plt.show()


def make(rm):
    return STRoadmapDrawer(rm)
