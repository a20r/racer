
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
        self.start = kwargs.get("start", point.make(0, 0))
        self.max_dist = kwargs.get("max_dist", 5)

    def resample(self, rm, num_points):
        node = point.make(self.start.x, self.start.y)
        rm.insert(node)
        bar = Bar("Generating Roadmap", max=num_points)
        for i in xrange(num_points):
            sample = point.get_random_point(self.width, self.height)
            rm.insert(sample)
            bar.next()
        bar.finish()
        return rm

    def generate(self, num_points):
        gd = grid.make(self.width, self.height, self.width, self.height)
        rm = roadmap.make(gd, self.max_dist)
        return self.resample(rm, num_points)


def make(**kwargs):
    return STRoadmapGenerator(**kwargs)
