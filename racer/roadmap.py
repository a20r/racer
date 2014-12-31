
import networkx as nx


class Roadmap(nx.Graph):

    def __init__(self, gd, max_dist, *args, **kwargs):
        self.gd = gd
        self.max_dist = max_dist
        nx.Graph.__init__(self, *args, **kwargs)

    def insert(self, sample):
        self.gd.insert(sample)
        for smpl in self.gd.get_nearest(sample):
            if smpl == sample:
                continue
            if smpl.dist_to(sample) <= self.max_dist:
                self.add_edge(smpl, sample)


def make(*args, **kwargs):
    return Roadmap(*args, **kwargs)
