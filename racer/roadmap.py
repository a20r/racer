
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
import path
import edmonds


class NoNodeFoundException(Exception):
    pass


class STRoadmap(nx.DiGraph):

    def get_first_nearest_node(self, pt, radius):
        for node in self.nodes():
            if node.euclid_dist(pt) <= radius:
                return node
        raise NoNodeFoundException("No node found")

    def get_path(self, s_pt, s_rad, e_pt, e_rad):
        s_node = self.get_first_nearest_node(s_pt, s_rad)
        e_node = self.get_first_nearest_node(e_pt, e_rad)
        s_path = nx.shortest_path(self, s_node, e_node)
        return path.make(s_path)


def make():
    return STRoadmap()
