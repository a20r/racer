

# because stupid pylint
__all__ = ["Axes3D"]

import pylab as plt
import warnings
from mpl_toolkits.mplot3d import Axes3D


class Drawer(object):

    def __init__(self, fig, ax):
        warnings.filterwarnings("ignore")
        self.fig = fig
        self.ax = ax

    def clear(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
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

    def get_xs_ys(self, node_list):
        xs = list()
        ys = list()
        for stp in node_list:
            xs.append(stp.x)
            ys.append(stp.y)

        return xs, ys

    def draw_temporal_nodes(self, rm, t_0, t_m):
        xs, ys, ts = self.get_xs_ys_ts(rm.nodes())
        axs = list()
        ays = list()
        for x, y, t in zip(xs, ys, ts):
            if t >= t_0 and t <= t_m:
                axs.append(x)
                ays.append(y)

        self.ax.scatter(axs, ays, alpha=0.5, zorder=9)
        return self

    def draw_temporal_edges(self, rm, t_0, t_m):
        for s_n, e_n in rm.edges():
            if s_n.t >= t_0 and e_n.t <= t_m:
                self.ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y], "k", alpha=0.2,
                             zorder=1)
        return self

    def draw_nodes(self, rm):
        xs, ys = self.get_xs_ys(rm.nodes())
        self.ax.scatter(xs, ys, alpha=1, c="r")
        return self

    def draw_edges(self, rm):
        for s_n, e_n in rm.edges():
            self.ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y], "k", alpha=0.2)
        return self

    def draw_path(self, path):
        for i, s_n in enumerate(path[:-1]):
            e_n = path[i + 1]
            self.ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y],
                         "r", linewidth=2)

        self.ax.scatter([path[-1].x], [path[-1].y], s=70, c="g", zorder=11)
        return self

    def draw_agent(self, ag, t):
        ag_pt = ag.get_position(t)
        xs = [ag_pt.x]
        ys = [ag_pt.y]
        self.ax.scatter(xs, ys, c="y", s=100, zorder=10)
        return self

    def show(self):
        plt.show()
        return self


def make(rm):
    return Drawer(rm)
