
import math
import stpoint
import random
import roadmap


class STRoadmapGenerator(object):

    def __init__(self, **kwargs):
        self.width = kwargs.get("width", 100)
        self.height = kwargs.get("height", 100)
        self.num_points = kwargs.get("num_points", 100)
        self.max_speed = kwargs.get("max_speed", 1)
        self.start = kwargs.get("start", (0, 0))
        self.max_time = 10

    def get_sample(self, ref):
        t_r = random.uniform(0.01 * self.max_time, self.max_time)
        theta = random.uniform(0, 2 * math.pi)
        r = random.uniform(0.001, self.max_speed * t_r)
        x = r * math.cos(theta) + ref.get_x()
        y = r * math.sin(theta) + ref.get_y()
        t = t_r + ref.get_t()
        return stpoint.make(x, y, t)

    def possible(self, stp1, stp2):
        if stp1.get_t() >= stp2.get_t():
            return False

        dist = stp1.euclid_dist(stp2)
        t_diff = (stp2 - stp1).get_t()
        return dist / t_diff <= self.max_speed

    def generate(self):
        rm = roadmap.make()
        samples = list()
        for i in xrange(self.num_points):
            if len(samples) == 0:
                t_r = self.max_time
                node = stpoint.make(self.start[0], self.start[1], 0)
                samples.append(node)

            else:
                t_r = random.choice(samples).get_t()

            ref = random.choice(samples)
            sample = self.get_sample(ref)
            rm.add_edge(ref, sample)

            if sample.within(0, self.width, 0, self.height):
                samples.append(sample)

            # makes it a graph
            for smpl in samples:
                if self.possible(smpl, sample):
                    rm.add_edge(smpl, sample)

        return rm


def make(**kwargs):
    return STRoadmapGenerator(**kwargs)
