
import networkx as nx
import path
import stpoint


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
        # mst = nx.minimum_spanning_tree(self)
        # path = nx.dijkstra_path(mst, s_node, e_node)
        path = nx.dijkstra_path(self, s_node, e_node)
        # norm_path = [stpoint.make(s_node.x, s_node.y, 0)]
        # for i, node in enumerate(path[1:]):
        #     px = node.x
        #     py = node.y
        #     pt = norm_path[i].t + abs(node.t - path[i].t)
        #     norm_path.append(stpoint.make(px, py, pt))

        # return norm_path
        return path


def make():
    return STRoadmap()
