
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import racer
import matplotlib.pyplot as plt

speed = 2
wait_time = 0.1
start = racer.Point(2, 0)
goal = racer.Point(2, 4)

fig = plt.figure()
ax_dr = fig.add_subplot(111)

ag = racer.Agent(
    racer.model.SinModel(2, 1, 1, 2),
    racer.model.LinearModel(0, 1))

ag2 = racer.Agent(
    racer.model.SinModel(-2, 2, 1, 2),
    racer.model.LinearModel(0, 1.3))

ag3 = racer.Agent(
    racer.model.SinModel(2, 2, 1, 2),
    racer.model.LinearModel(0, 2))

strg = racer.RoadmapGenerator(
    start=start, width=4, height=4, max_dist=0.5)

rm = strg.generate(300)
search = racer.Search(rm, speed, wait_time)
path, tree = search.get_path(start, goal, ag, ag2, ag3)

dr = racer.Drawer(fig, ax_dr)

for i, p in enumerate(path[1:]):
    # ax_dr.set_xlabel("X Position [m]")
    # ax_dr.set_ylabel("Y Position [m]")
    # ax_dr.set_zlabel("Time [s]")
    dr.draw_temporal_nodes(tree, 0, p.t)
    dr.draw_temporal_edges(tree, 0, p.t)
    dr.draw_path(path[:(i + 2)])
    dr.draw_agent(ag, p.t)
    dr.draw_agent(ag2, p.t)
    dr.draw_agent(ag3, p.t)
    plt.xlim([-0.1, 4.1])
    plt.ylim([-0.1, 4.1])
    plt.savefig("figs/tree_{}.pdf".format(i), bbox_inches="tight")
    dr.clear()
