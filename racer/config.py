
class Problem(object):

    def __init__(self, **kwargs):
        self.width = kwargs.get("width", 640)
        self.height = kwargs.get("height", 480)
        self.num_nodes = kwargs.get("num_nodes", 500)
        self.epsilon = kwargs.get("epsilon", 7)
        self.goal_radius = kwargs.get("goal_radius", 7)


