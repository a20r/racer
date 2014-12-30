
import networkx as nx
import path
import agent
import heapq
import stpoint


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

    def _get_path(self, s_pt, s_rad, e_pt, e_rad):
        s_node = self.get_first_nearest_node(s_pt, s_rad)
        e_node = self.get_first_nearest_node(e_pt, e_rad)
        s_path = nx.shortest_path(self, s_node, e_node)
        return path.make(s_path)

    def get_st_neighbours(self, node, speed, wait_time):
        st_neighbours = list()
        st_neighbours.append(stpoint.make(node.x, node.y, node.t + wait_time))

        for nbr in self.neighbours(node.to_point()):
            dist = node.dist_to(nbr)
            t = dist / speed + node.get_t()
            stp = stpoint.make(nbr.x, nbr.y, t)
            st_neighbours.append(stp)

        return st_neighbours


    def get_path(self, s_pt, s_rad, e_pt, e_rad, speed, wait_time, *agents):
        s_node = self.get_first_nearest_node(s_pt, s_rad)
        e_node = self.get_first_nearest_node(e_pt, e_rad)
        penalties = dict()
        open_set = [(0, s_node.to_st_point_2d(0))]

        while len(open_set) > 0:
            current = heapq.heappop(open_set)
            if current == e_node:
                return True

            st_neighbours = self.get_st_neighbours(current, speed, wait_time)
            for nbr in st_neighbours:
                pass


def make():
    return Roadmap()
