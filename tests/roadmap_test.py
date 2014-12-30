
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import racer

ag = racer.Agent(
    racer.model.SinModel(2, 2, 1, 2),
    racer.model.LinearModel(0, 3)
)

ag2 = racer.Agent(
    racer.model.SinModel(-2, 2, 1, 2),
    racer.model.LinearModel(0, 1)
)


start = racer.Point(2, 0)
strg = racer.RoadmapGenerator(
    start=start, width=5, height=5, max_dist=1
)
rm, _ = strg.generate(1000)
dr = racer.Drawer()

# goal = racer.Point(2, 4)
# goal_rad = 1
# start_rad = 0
# path = rm.get_path(start, start_rad, goal, goal_rad)

# dr.draw_edges(rm)
dr.draw_nodes(rm)
# dr.draw_path(path)
# dr.draw_agent(ag, path.get_max_time())
# dr.draw_agent(ag2, path.get_max_time())
dr.show()

# anmtr = racer.Animator(path, ag, ag2)
# anmtr.run()
