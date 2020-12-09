# Shape Objects

class shape:
    def __init__(self, sh_sides, sh_side_length):
        self.total_degrees = 360
        self.sides = sh_sides
        self.corner_angle = self.total_degrees / sh_sides
        self.side_length = sh_side_length


def initialise_shapes(max_sides, side_length_x):
    max_sides = max(max_sides, 3)
    return [shape(sh_sides=side_x, sh_side_length=side_length_x) for side_x in range(3, max_sides+1)]

