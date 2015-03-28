
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
ax_an = fig.add_subplot(111)

ag = racer.Agent(
    racer.model.SinModel(2, 1, 1, 2),
    racer.model.LinearModel(0, 1))

ag2 = racer.Agent(
    racer.model.SinModel(-2, 2, 1, 2),
    racer.model.LinearModel(0, 1.3))

strg = racer.RoadmapGenerator(
    start=start, width=4, height=4, max_dist=0.5)

rm = strg.generate(300)
dr = racer.Drawer(fig, ax_an)

dr.draw_edges(rm)
dr.draw_nodes(rm)
ax_an.set_xlabel("X Position [m]")
ax_an.set_ylabel("Y Position [m]")
plt.xlim([-0.1, 4.1])
plt.ylim([-0.1, 4.1])
plt.savefig("figs/roadmap.pdf", bbox_inches="tight")
dr.show()
