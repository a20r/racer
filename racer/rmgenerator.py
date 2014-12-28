
import math
import point
import stpoint
import random
import roadmap
import agent
import grid
from progress.bar import Bar


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
        self.num_edge_samples = 10
        self.dist_w = 0.0
        self.cost_w = 1
        self.cost_scal = 10

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
        max_cost = 0
        for i in xrange(self.num_edge_samples + 1):
            x = n1.x + i * x_slope
            y = n1.y + i * y_slope
            cost = pdf(x, y)
            if cost > max_cost:
                max_cost = cost

        ret_cost = self.cost_scal * max_cost
        return ret_cost

    def generate(self):
        rm = roadmap.make()
        gd = grid.make(5, 5, 5, 5)
        samples = list()
        node = stpoint.make(self.start.x, self.start.y, 0)
        rm.add_edge(node, node, weight=0)
        gd.insert(node)
        samples.append(node)
        bar = Bar("Generating Roadmap", max=self.num_points)
        for i in xrange(self.num_points):
            ref = random.choice(samples)
            sample = self.get_sample(ref)
            rm.add_edge(ref, sample, weight=self.get_cost(ref, sample))

            if sample.within(0, self.width, 0, self.height):
                samples.append(sample)
                gd.insert(sample)

            # makes it a graph
            for smpl in gd.get_nearest(sample):
                if smpl == sample:
                    continue

                within_distance = smpl.euclid_dist(sample) <= self.max_dist
                within_time = abs(sample.t - smpl.t) <= self.max_time
                if within_distance and within_time:
                    if smpl.t < sample.t and self.possible(smpl, sample):
                        cost = self.get_cost(smpl, sample)
                        rm.add_edge(smpl, sample, weight=cost)
                    elif smpl.t > sample.t and self.possible(sample, smpl):
                        cost = self.get_cost(sample, smpl)
                        rm.add_edge(sample, smpl, weight=cost)
            bar.next()

        bar.finish()
        return rm


def make(**kwargs):
    return STRoadmapGenerator(**kwargs)
