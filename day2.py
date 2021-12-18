import numpy as np

data_path = 'inputs/day2.txt'

direction, magnitude = np.loadtxt(data_path, delimiter=' ', dtype=str, unpack=True)

magnitude = magnitude.astype(np.int64)

unique_directions = np.unique(direction, return_inverse=True)

x_directions = ('forward')
y_directions = {'up': -1,
                'down': 1,
                'forward': 0}

x_vector = np.isin(direction, x_directions) * magnitude
y_vector = np.vectorize(y_directions.get)(direction) * magnitude

x_position = np.sum(x_vector)
y_position = np.sum(y_vector)

answer1 = x_position * y_position

# section 2

aim = np.cumsum(y_vector)
y_vector = x_vector * aim
y_position = y_vector.sum()

answer2 = x_position * y_position
