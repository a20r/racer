
import networkx as nx
import path
import agent
import heapq
import stpoint


class NoNodeFoundException(Exception):
    pass


class NoPathFoundException(Exception):
    pass


class Search(object):

    REPEAT_COST_SCAL = 0.1
    NUM_EDGE_SAMPLES = 10
    COST_SCAL = 10
    GOAL_RADIUS = 1

    def __init__(self, rm, speed, wait_time):
        self.rm = rm
        self.speed = speed
        self.wait_time = wait_time

    def get_cost(self, n1, n2, *agents):
        max_cost = 0
        pdf = agent.get_pdf(n1.t, n2.t, *agents)
        x_slope = (n2.x - n1.x) / self.NUM_EDGE_SAMPLES
        y_slope = (n2.y - n1.y) / self.NUM_EDGE_SAMPLES

        for i in xrange(self.NUM_EDGE_SAMPLES + 1):
            x = n1.x + i * x_slope
            y = n1.y + i * y_slope
            cost = pdf(x, y)
            if cost > max_cost:
                max_cost = cost

        return max_cost

    def get_st_neighbours(self, node):
        st_neighbours = list()
        st_neighbours.append(stpoint.make(
            node.x, node.y, node.t + self.wait_time))
        for nbr in self.rm.neighbors(node.to_point()):
            dist = node.euclid_dist(nbr)
            t = dist / self.speed + node.get_t()
            stp = stpoint.make(nbr.x, nbr.y, t)
            st_neighbours.append(stp)

        return st_neighbours

    def get_path(self, s_pt, e_pt, *agents):
        self.rm.insert(s_pt)
        self.rm.insert(e_pt)
        num_visited = dict()
        parents = dict()
        tree = nx.DiGraph()
        st_pt = s_pt.to_st_point_2d(0)
        max_costs = {st_pt: 0}
        open_set = [(0, st_pt)]

        while len(open_set) > 0:
            _, current = heapq.heappop(open_set)
            if current.to_point().dist_to(e_pt) < self.GOAL_RADIUS:
                ret_path = self.backtrack_path(parents, current)
                return path.make(ret_path), tree

            for nr in self.get_st_neighbours(current):
                parents[nr] = current
                tree.add_edge(current, nr)
                nr_pt = nr.to_point()
                nr_cost = self.COST_SCAL * self.get_cost(current, nr, *agents)

                if nr_cost < max_costs[current]:
                    nr_cost = max_costs[current]

                max_costs[nr] = nr_cost

                if nr_pt in num_visited:
                    r_cost = self.REPEAT_COST_SCAL * num_visited[nr_pt]
                    num_visited[nr_pt] += 1
                else:
                    r_cost = 0
                    num_visited[nr_pt] = 1

                total_cost = nr_cost + r_cost
                heapq.heappush(open_set, (total_cost, nr))

        raise NoPathFoundException("No path found from %s to %s"
                                   % (repr(s_pt), repr(e_pt)))

    def backtrack_path(self, parents, goal):
        path_list = [goal]
        current = parents[goal]
        while True:
            path_list.append(current)
            try:
                current = parents[current]
            except KeyError:
                path_list.reverse()
                return path_list
