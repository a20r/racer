
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import racer

ag = racer.Agent(
    racer.model.SinModel(2, 1, 1, 2),
    racer.model.LinearModel(0, 2)
)

ag2 = racer.Agent(
    racer.model.SinModel(-2, 1, 1, 2),
    racer.model.LinearModel(0, 1)
)


strg = racer.STRoadmapGenerator(num_points=1000, agents=[ag])
rm = strg.generate()
rmdr = racer.STRoadmapDrawer(rm)

start = racer.Point(0, 0)
goal = racer.Point(3.5, 3.5)
path = rm.get_path(start, 0, goal, 1)

# rmdr.draw_nodes()
rmdr.draw_path(path)
rmdr.draw_agent(ag, path[-1].t)
rmdr.draw_agent(ag2, path[-1].t)
rmdr.show()

anmtr = racer.Animator(path, ag, ag2)
anmtr.run()
