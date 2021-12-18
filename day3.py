import numpy as np

data_path = 'inputs/day3.txt'

data = np.loadtxt(data_path,dtype=str)

data = np.array([list(i) for i in data]).astype(bool)

gamma_binary = (np.sum(data, axis=0)/len(data) > 0.5).astype(int)
epsilon_binary = 1-gamma_binary

gamma_decimal = int("".join(gamma_binary.astype(str)), 2)
epsilon_decimal = int("".join(epsilon_binary.astype(str)), 2)

answer1 = gamma_decimal * epsilon_decimal

# section 2

mask = np.ones(len(data), dtype=bool)
for i in range(data.shape[1]):
    mask = mask * (data[:, i] == (np.sum(data[mask, i])/len(data[mask]) >= 0.5))


answer2 = 1