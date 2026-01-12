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
            #TIY-15-4 code under
            # x_direction = choice([1])
            # y_direction = choice([-1, 1])
            # x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            # y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            #till here

            x_step = self.get_step_x()
            y_step = self.get_step_y()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    # TIY 15-5
    def get_step_x(self):
        """a method to calculate the x steps"""
        x_direction = choice([-1,1])
        x_distance = choice([0,1,2,3,4,5])
        return x_direction * x_distance

    def get_step_y(self):
        """a method to calculate the y steps"""
        y_direction = choice([-1,1])
        y_distance = choice([0,1,2,3,4,5])
        return y_direction * y_distance