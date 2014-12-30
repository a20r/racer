
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

    def resample(self, rm, gd, num_points):
        node = point.make(self.start.x, self.start.y)
        gd.insert(node)
        bar = Bar("Generating Roadmap", max=num_points)
        for i in xrange(num_points):
            sample = point.get_random_point(self.width, self.height)
            gd.insert(sample)

            for smpl in gd.get_nearest(sample):
                if smpl == sample:
                    continue
                if smpl.dist_to(sample) <= self.max_dist:
                    rm.add_edge(smpl, sample)

            bar.next()
        bar.finish()
        return rm, gd

    def generate(self, num_points):
        rm = roadmap.make()
        gd = grid.make(self.width, self.height, self.width, self.height)
        return self.resample(rm, gd, num_points)


def make(**kwargs):
    return STRoadmapGenerator(**kwargs)
