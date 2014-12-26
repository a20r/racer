
import matplotlib.pyplot as plt


class Animator(object):

    def __init__(self, path, *agents):
        plt.ion()
        self.fig = plt.figure("Uncertainty Map")
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("X Location")
        self.ax.set_ylabel("Y Location")
        self.path = path
        self.agents = agents
        self.agent_plots = [plt.scatter([], []) for _ in agents]
        self.pln_plot = plt.scatter([], [])

    def update(self, t):
        pln_pos = self.path(t)
        self.pln_plot.remove()
        self.pln_plot = plt.scatter(
            [pln_pos.x], [pln_pos.y], marker="o", color="b", s=40)

        for i, ag in enumerate(self.agents):
            ag_pos = ag.get_position(t)
            self.agent_plots[i].remove()
            self.agent_plots[i] = plt.scatter(
                [ag_pos.x], [ag_pos.y], marker="^", color="r", s=40)

        plt.draw()
        plt.pause(0.01)

    def run(self):
        time_step = 0.05
        t = 0
        while True:
            while t < self.path[-1].t:
                self.update(t)
                t += time_step
            t = 0
