
class Grid(object):

    def __init__(self, width, height, a_width, a_height):
        self.width = width
        self.height = height
        self.a_width = a_width
        self.a_height = a_height
        self.grid = [[list() for i in xrange(width)] for j in xrange(height)]

    def map_val(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def insert(self, st_p):
        i, j = self.transform(st_p)
        self.grid[j][i].append(st_p)
        return self

    def transform(self, st_p):
        i = j = None
        if st_p.x >= self.a_width:
            i = self.width - 1
        elif st_p.x <= 0:
            i = 0

        if st_p.y >= self.a_height:
            j = self.height - 1
        elif st_p.y <= 0:
            j = 0

        if i is None:
            i = int(self.map_val(st_p.x, 0, self.a_width, 0, self.width - 1))

        if j is None:
            j = int(self.map_val(st_p.y, 0, self.a_height, 0, self.height - 1))

        return i, j

    def get(self, i, j):
        return self.grid[j][i]

    def get_nearest(self, st_p):
        i, j = self.transform(st_p)
        i_diffs = [-1, 0, 1]
        j_diffs = [-1, 0, 1]
        if i == 0:
            del i_diffs[0]
        if i == self.width - 1:
            del i_diffs[2]
        if j == 0:
            del j_diffs[0]
        if j == self.height - 1:
            del j_diffs[2]

        closest = list()

        for i_diff in i_diffs:
            for j_diff in j_diffs:
                closest.extend(self.get(i + i_diff, j + j_diff))

        return closest


def make(*args):
    return Grid(*args)
