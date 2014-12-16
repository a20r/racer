
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import racer

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

strg = racer.STRoadmapGenerator(num_points=1000)
rm = strg.generate()
xs, ys, ts = rm.get_xs_ys_ts()

ax.scatter(xs, ys, ts)

# for s_n, e_ns in rm.get_graph().iteritems():
    # for e_n in e_ns:
        # ax.plot([s_n.x, e_n.x], [s_n.y, e_n.y], [s_n.t, e_n.t])

plt.show()
