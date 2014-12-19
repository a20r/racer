
import networkx as nx

class NoNodeFoundException(Exception):
    pass


class STRoadmap(nx.DiGraph):

    def get_best_node(self, pt, radius):
        for node in self.nodes():
            if node.euclid_dist(pt) <= radius:
                return node
        raise NoNodeFoundException("No node found")

    def get_path(self, s_pt, s_rad, e_pt, e_rad):
        s_node = self.get_best_node(s_pt, s_rad)
        e_node = self.get_best_node(e_pt, e_rad)
        return nx.dijkstra_path(self, s_node, e_node)


def make():
    return STRoadmap()
