
import math
import point
import tree


class Planner(object):

    def __init__(self, problem, **kwargs):
        self.model_list = kwargs.get("model_list", list())
        self.problem = problem

    def rrt_step(self, p1, p2):
        if p1.dist_to(p2) < self.problem.epsilon:
            return p2

        else:
            theta = math.atan2(
                p2.get_y() - p1.get_y(),
                p2.get_x() - p1.get_x()
            )

            return point.Point(
                p1.get_x() + self.problem.epsilon * math.cos(theta),
                p1.get_y() + self.problem.epsilon * math.sin(theta)
            )

    def plan(self, start, goal):
        node_tree = tree.Tree(start)
        node_list = [start]

        for i in xrange(self.problem.num_nodes):
            random_point = point.get_random_point(
                self.problem.width,
                self.problem.height
            )

            min_node = None

            for node in node_list:
                if min_node is None:
                    min_node = node
                else:
                    n_dist = node.dist_to(random_point)
                    m_dist = min_node.dist_to(random_point)
                    if n_dist < m_dist:
                        min_node = node

            new_node = self.rrt_step(min_node, random_point)
            node_list.append(new_node)
            min_node.add_child(tree.Tree(new_node))

            if goal.dist_to(new_node) < self.problem.goal_radius:
                return new_node.get_path_to_root()


