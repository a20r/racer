
class STRoadmap(object):

    def __init__(self):
        self.graph = dict()
        self.weights = dict()

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

    def get_weight(self, n1, n2):
        return self.weights[(n1, n2)]

    def shortest_path(self, n1, n2):
        return list()
