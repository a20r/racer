
import math
import point


class Agent(object):

    def __init__(self, model_x, model_y):
        self.model_x = model_x
        self.model_y = model_y
        self.delta_t = 0.1
        self.k = 3

    def get_normal_dist(self, X, std):
        coeff = 1.0 / (std * math.sqrt(2 * math.pi))
        return coeff * math.exp(- math.pow(X, 2) / (2.0 * math.pow(std, 2)))

    def get_position(self, t_0):
        return point.Point(self.model_x(t_0), self.model_y(t_0))

    def get_probability(self, x, y, t_0, t_m):
        # t_0 is the current time, don't fuck this up
        assert t_0 < t_m
        t = t_0
        prob_sum = 0.0
        num_samples = (t_m - t_0) / self.delta_t

        while t < t_m:
            pos = self.get_position(t)
            dist = pos.dist_to(point.Point(x, y))
            prob = self.get_normal_dist(dist, self.k * (t - t_0) + 1)
            prob_sum += prob
            t += self.delta_t

        return prob_sum / num_samples
