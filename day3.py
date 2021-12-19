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

mask_o2 = np.ones(len(data), dtype=bool)
mask_co2 = np.ones(len(data), dtype=bool)
for i in range(data.shape[1]):
    mask_o2 *= (data[:, i] == (np.sum(data[mask_o2, i]) / len(data[mask_o2]) >= 0.5))
    if ~np.isin(np.sum(data[mask_co2, i]) / len(data[mask_co2]), (0, 1)):
        mask_co2 *= (data[:, i] != (np.sum(data[mask_co2, i]) / len(data[mask_co2]) >= 0.5))

o2_decimal = int("".join(data[mask_o2].astype(int).astype(str)[0]), 2)
co2_decimal = int("".join(data[mask_co2].astype(int).astype(str)[0]), 2)

answer2 = o2_decimal * co2_decimal
