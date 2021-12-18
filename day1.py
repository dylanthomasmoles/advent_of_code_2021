import numpy as np

data_path = 'inputs/day1.txt'

data = np.loadtxt(data_path, dtype=np.int64)

answer1 = np.sum((data[1:] - data[:-1]) > 0)

# section 2

data_convolved = np.convolve(np.ones(3), data, mode='valid')

answer2 = np.sum((data_convolved[1:] - data_convolved[:-1]) > 0)
