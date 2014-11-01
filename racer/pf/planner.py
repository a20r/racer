
import random
import math
import point


class Planner(object):

    def __init__(self):
        # self.problem = problem
        self.K = 10000000
        self.num_samples = 10
        self.sample_radius = 10

    def goal_potential(self, dist):
        return pow(dist, 2.0)

    def obstacle_potential(self, pdf_val):
        # This is going to require some trial and error
        return self.K * pdf_val

    def plan(self, start, goal, pdf):
        min_potential = None
        vel = point.Point(0, 0)
        for _ in xrange(self.num_samples):
            angle = random.random() * 2 * math.pi
            x_s = start.x + self.sample_radius * math.cos(angle)
            y_s = start.y + self.sample_radius * math.sin(angle)
            p_s = point.Point(x_s, y_s)
            dist_to_goal = p_s.dist_to(goal)
            g_p = self.goal_potential(dist_to_goal)
            o_p = self.obstacle_potential(pdf(x_s, y_s))
            potential = o_p + g_p
            # print o_p, g_p

            if min_potential is None or potential < min_potential:
                min_potential = potential
                vel.set_x(x_s - start.x)
                vel.set_y(y_s - start.y)

        return vel.to_unit_vector()
