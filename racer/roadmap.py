
class PathNotFoundException(Exception):
    pass


class STRoadmap(object):

    def __init__(self):
        self.graph = dict()
        self.nodes = set()
        self.weights = dict()

    def get_graph(self):
        return self.graph

    def add_edge(self, n1, n2):
        """
        The roadmap is a directed graph, in which a node n_0 and n_1
        can only be connected if time(n_0) < time(n_1). This will probably
        make more sense later on when there is more documentation.
        """

        assert(n1.get_t() < n2.get_t())

        try:
            self.graph[n1].append(n2)
        except KeyError:
            self.graph[n1] = [n2]

        self.nodes.add(n1)
        self.nodes.add(n2)

        return self

    def has_edge(self, n1, n2):
        try:
            return n2 in self.graph[n1]
        except:
            return False

    def add_weight(self, n1, n2, weight):
        """
        Adds weight to an edge and creates the edge if it does not
        exist already
        """

        if not self.has_edge(n1, n2):
            self.add_edge(n1, n2)

        self.weights[(n1, n2)] = weight
        return self

    def get_nodes(self):
        return list(self.nodes)

    def get_weight(self, n1, n2):
        return self.weights[(n1, n2)]

    def get_xs_ys_ts(self):
        xs = list()
        ys = list()
        ts = list()
        for stp in self.get_nodes():
            xs.append(stp.x)
            ys.append(stp.y)
            ts.append(stp.t)

        return xs, ys, ts

    def path(self, s_pt, g_pt, radius):
        assert(s_pt in self.graph.keys())

        closed_set = set()
        open_set = set([s_pt])
        came_from = dict()
        g_score = dict()
        f_score = dict()

        g_score[s_pt] = 0
        f_score[s_pt] = s_pt.euclid_dist(g_pt)

        while len(open_set) > 0:
            current = None
            min_f_score = None
            for node in open_set:
                if current is None or f_score[node] < min_f_score:
                    current = node
                    min_f_score = f_score[node]

            print current
            print g_pt
            print "================="

            if current.euclid_dist(g_pt) < radius:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            closed_set.add(current)

            for neighbour in self.graph[current]:
                # if neighbour in closed_set:
                    # continue
                t_g_score = g_score[current] + current.euclid_dist(neighbour)

                if not neighbour in open_set or t_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = t_g_score
                    goal_dist = neighbour.euclid_dist(g_pt)
                    f_score[neighbour] = g_score[neighbour] + goal_dist

                    if not neighbour in open_set:
                        open_set.add(neighbour)

        raise PathNotFoundException()

    def reconstruct_path(self, came_from, current):
        total_path = [current]

        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)

        return total_path


def make():
    return STRoadmap()
