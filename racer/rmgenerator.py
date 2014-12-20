
import math
import point
import stpoint
import random
import roadmap
import agent
import networkx as nx


class STRoadmapGenerator(object):

    def __init__(self, **kwargs):
        self.width = kwargs.get("width", 100)
        self.height = kwargs.get("height", 100)
        self.num_points = kwargs.get("num_points", 100)
        self.max_speed = kwargs.get("max_speed", 2)
        self.start = kwargs.get("start", point.Point(0, 0))
        self.agents = kwargs.get("agents", list())
        self.max_time = 1
        self.max_dist = 1
        self.num_edge_samples = 15
        self.dist_w = 0.0
        self.cost_w = 1

    def get_start(self):
        return stpoint.make(self.start.x, self.start.y, 0)

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

    def get_cost(self, n1, n2):
        dist = n1.euclid_dist(n2)
        if len(self.agents) == 0:
            return dist

        pdf = agent.get_pdf(n1.t, n2.t, *self.agents)
        x_slope = (n2.x - n1.x) / self.num_edge_samples
        y_slope = (n2.y - n1.y) / self.num_edge_samples
        cost = 0
        for i in xrange(self.num_edge_samples):
            x = n1.x + i * x_slope
            y = n1.y + i * y_slope
            cost += pdf(x, y)

        return self.cost_w * cost + self.dist_w * dist

    def generate(self):
        rm = roadmap.make()
        samples = list()
        for i in xrange(self.num_points):
            if len(samples) == 0:
                node = stpoint.make(self.start.x, self.start.y, 0)
                samples.append(node)

            ref = random.choice(samples)
            sample = self.get_sample(ref)
            rm.add_edge(ref, sample, weight=ref.euclid_dist(sample))

            if sample.within(0, self.width, 0, self.height):
                samples.append(sample)

            # makes it a graph
            for smpl in samples:
                within_distance = smpl.euclid_dist(sample) <= self.max_dist
                is_move_possible = self.possible(smpl, sample)
                within_time = abs(sample.t - smpl.t) <= self.max_time
                if within_distance and is_move_possible and within_time:
                    if smpl.t < sample.t:
                        cost = self.get_cost(smpl, sample)
                        rm.add_edge(smpl, sample, weight=cost)
                    else:
                        cost = self.get_cost(sample, smpl)
                        rm.add_edge(sample, smpl, weight=cost)

        return rm


def make(**kwargs):
    return STRoadmapGenerator(**kwargs)
