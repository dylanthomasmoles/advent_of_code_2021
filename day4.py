import numpy as np

data_path = 'inputs/day4.txt'

bingo_numbers = np.loadtxt(data_path, delimiter=',', max_rows=1, dtype=int)

bingo_boards_input = np.loadtxt(data_path, delimiter='\n', skiprows=2, dtype=str)
bingo_boards_flat = np.array([i.split() for i in bingo_boards_input]).astype(int)
bingo_boards = np.reshape(bingo_boards_flat, (-1, 5, 5))

bingo_dabs = np.zeros_like(bingo_boards, dtype=int)
for idx, call in enumerate(bingo_numbers):
    bingo_dabs = bingo_dabs + (bingo_boards == call)

    rows_count = bingo_dabs.sum(axis=1)
    cols_count = bingo_dabs.sum(axis=2)

    winners = np.bitwise_or((rows_count == 5).any(axis=1), (cols_count == 5).any(axis=1))
    if np.sum(winners) > 0:
        winning_call = call
        print("Bingo!")
        winning_boards = bingo_boards[winners]
        print(winning_boards)
        winning_dabs = bingo_dabs[winners]
        print(winning_dabs)
        break

answer1 = winning_call * np.sum(winning_boards[~winning_dabs.astype(bool)])

# section 2

remaining_boards = bingo_boards[~winners]
remaining_dabs = bingo_dabs[~winners]

remaining_numbers = bingo_numbers[(idx+1):]

for call in remaining_numbers:
    remaining_dabs = remaining_dabs + (remaining_boards == call)

    rows_count = remaining_dabs.sum(axis=1)
    cols_count = remaining_dabs.sum(axis=2)

    winners = np.bitwise_or((rows_count == 5).any(axis=1), (cols_count == 5).any(axis=1))

    if remaining_boards.shape[0] == winners.sum():
        winning_call = call
        print("...bingo?")
        winning_boards = remaining_boards
        print(winning_boards)
        winning_dabs = remaining_dabs
        print(winning_dabs)
        break

    remaining_boards = remaining_boards[~winners]
    remaining_dabs = remaining_dabs[~winners]

answer2 = winning_call * np.sum(winning_boards[~winning_dabs.astype(bool)])