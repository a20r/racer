
import networkx as nx
import path
import agent


class NoNodeFoundException(Exception):
    pass


class Roadmap(nx.Graph):

    def get_first_nearest_node(self, pt, radius):
        for node in self.nodes():
            if node.euclid_dist(pt) <= radius:
                return node
        raise NoNodeFoundException("No node found")

    def get_cost(self, n1, n2, *agents):
        max_cost = 0
        cost_scal = 10
        num_edge_samples = 10
        pdf = agent.get_pdf(n1.t, n2.t, *agents)
        x_slope = (n2.x - n1.x) / num_edge_samples
        y_slope = (n2.y - n1.y) / num_edge_samples

        for i in xrange(num_edge_samples + 1):
            x = n1.x + i * x_slope
            y = n1.y + i * y_slope
            cost = pdf(x, y)
            if cost > max_cost:
                max_cost = cost

        return cost_scal * max_cost

    def get_path(self, s_pt, s_rad, e_pt, e_rad):
        s_node = self.get_first_nearest_node(s_pt, s_rad)
        e_node = self.get_first_nearest_node(e_pt, e_rad)
        s_path = nx.shortest_path(self, s_node, e_node)
        return path.make(s_path)


def make():
    return Roadmap()
