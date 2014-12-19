
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import networkx as nx
import racer

strg = racer.STRoadmapGenerator(num_points=1000)
rm = strg.generate()
rmdr = racer.STRoadmapDrawer(rm)

start = racer.Point(0, 0)
goal = racer.Point(3, 3)
path = rm.get_path(start, 0, goal, 1)

rmdr.draw_nodes()
rmdr.draw_path(path)
rmdr.show()
