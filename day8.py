# PART 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?

# each of the first ten signal patterns represent a unique digit from 0 to 9
# deduce from the number of the signal_lines which digit each letter corresponds
# to and translate the resulting number output of 4 digits after |
from typing import Tuple, List


def parse_file(input_file: str) -> List[List[int]]:
    all_puzzles = []
    with open(input_file, 'r') as file:
        all_lines = [[st for st in line.split()] for line in file]
        for line in all_lines:
            signal_patterns = line[:10]
            encoded_output = line[11:]
            all_puzzles.append([signal_patterns, encoded_output])

    return all_puzzles


if __name__ == '__main__':

    all_puzzles = parse_file("input8.csv")

    # answer_1 = simulate(all_initial_timers)
    # answer_2 = simulate_faster(all_initial_timers, days_to_run=256)

    # print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
