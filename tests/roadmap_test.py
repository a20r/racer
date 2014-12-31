
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
# ax_dr = fig.add_subplot(122, projection="3d")

ag = racer.Agent(
    racer.model.SinModel(2, 3, 1, 2),
    racer.model.LinearModel(0, 3))

ag2 = racer.Agent(
    racer.model.SinModel(-2, 2, 1, 2),
    racer.model.LinearModel(0, 1))


strg = racer.RoadmapGenerator(
    start=start, width=4, height=4, max_dist=0.1)

rm = strg.generate(5000)
search = racer.Search(rm, speed, wait_time)
path, tree = search.get_path(start, goal, ag, ag2)
# dr = racer.Drawer(fig, ax_dr)
anmtr = racer.Animator(fig, ax_an, path, ag, ag2)

# dr.draw_edges(rm)
# dr.draw_nodes(rm)
# dr.draw_temporal_nodes(tree)
# dr.draw_path(path)
# dr.draw_agent(ag, path.get_max_time())
# dr.draw_agent(ag2, path.get_max_time())
# dr.show()
anmtr.run()
