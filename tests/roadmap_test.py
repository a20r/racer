
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import racer

ag = racer.Agent(
    racer.model.SinModel(2, 3, 1, 2),
    racer.model.LinearModel(0, 3)
)

ag2 = racer.Agent(
    racer.model.SinModel(-2, 4, 1, 2),
    racer.model.LinearModel(0, 1)
)


start = racer.Point(2, 0)
strg = racer.STRoadmapGenerator(num_points=1000, start=start, agents=[ag, ag2])
rm = strg.generate()
rmdr = racer.STRoadmapDrawer(rm)

goal = racer.Point(2, 4)
goal_rad = 1
start_rad = 0
path = rm.get_path(start, start_rad, goal, goal_rad)

# rmdr.draw_nodes()
rmdr.draw_path(path)
rmdr.draw_agent(ag, path[-1].t)
rmdr.draw_agent(ag2, path[-1].t)
rmdr.show()

anmtr = racer.Animator(path, ag, ag2)
anmtr.run()
