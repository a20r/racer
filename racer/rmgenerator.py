
import math
import point
import stpoint
import random
import roadmap
import grid
from progress.bar import Bar


class RoadmapGenerator(object):

    def __init__(self, **kwargs):
        self.width = kwargs.get("width", 100)
        self.height = kwargs.get("height", 100)
        self.num_points = kwargs.get("num_points", 1000)
        self.start = kwargs.get("start", point.make(0, 0))
        self.max_dist = kwargs.get("max_dist", 5)

    def generate(self):
        rm = roadmap.make()
        gd = grid.make(5, 5, 5, 5)
        node = point.make(self.start.x, self.start.y)
        gd.insert(node)
        bar = Bar("Generating Roadmap", max=self.num_points)
        for i in xrange(self.num_points):
            sample = point.get_random_point(self.width, self.height)
            gd.insert(sample)

            for smpl in gd.get_nearest(sample):
                if smpl == sample:
                    continue
                if smpl.dist_to(sample) <= self.max_dist:
                    rm.add_edge(smpl, sample)

            bar.next()
        bar.finish()
        return rm


def make(**kwargs):
    return STRoadmapGenerator(**kwargs)
