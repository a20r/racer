
class Planner(object):

    def __init__(self, problem):
        self.problem = problem
        self.K = 100
        self.num_samples = 10

    def goal_potential(self, dist):
        return pow(dist, 2.0)

    def obstacle_potential(self, pdf_val):
        # This is going to require some trial and error
        return self.K * pdf_val

    def plan(self, start, goal, pdf):
        pass
