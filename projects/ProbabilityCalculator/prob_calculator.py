import copy
import random
from collections import Counter
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.contents = []
        for color, count in self.__dict__.items():
            if type(count) == int:
                print(color, count)
                self.contents += ([color] * count)

    def draw(self, number):
        if number > len(self.contents):
            number = len(self.contents)
        draw = random.sample(self.contents, number)
        for ball in draw:
            self.contents.remove(ball)
        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n_successes = 0
    expected_balls_list = []
    for color, count in expected_balls.items():
        expected_balls_list += ([color] * count)

    for i in range(num_experiments):
        tmp_hat = copy.deepcopy(hat)
        draw = tmp_hat.draw(num_balls_drawn)
        if not (Counter(expected_balls_list) - Counter(draw)):
            n_successes += 1

    probability = n_successes / num_experiments
    return probability
