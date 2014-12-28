
import networkx as nx
import path
import stpoint


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

    def _get_path(self, s_pt, s_rad, e_pt, e_rad):
        # Doesn't work, but could work if I tweaked with the graph
        # generation
        s_node = self.get_first_nearest_node(s_pt, s_rad)
        e_node = self.get_first_nearest_node(e_pt, e_rad)
        mst = nx.minimum_spanning_tree(self.to_undirected())
        s_path = nx.dijkstra_path(mst, s_node, e_node)
        norm_path = [stpoint.make(s_node.x, s_node.y, 0)]
        for i, node in enumerate(s_path[1:]):
            px = node.x
            py = node.y
            pt = norm_path[i].t + abs(node.t - s_path[i].t)
            norm_path.append(stpoint.make(px, py, pt))

        return path.make(norm_path)


def make():
    return STRoadmap()
