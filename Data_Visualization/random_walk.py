from random import choice

class RandomWalk:
    """a class to represent a random walk"""

    def __init__(self,n_points = 5000):
        """Initialize attributes for random walk"""
        self.n_points = n_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the points in the walk"""
        while len(self.x_values) < self.n_points:
            x_direction = choice([-1,1])
            y_direction = choice([-1,1])

            x_distance = choice([0,1,2,3,4,5])
            y_distance = choice([0,1,2,3,4,5])

            x_step = x_direction * x_distance
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

