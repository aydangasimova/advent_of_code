from typing import Tuple, Set, List


# How many dots are visible after completing just the first fold instruction on your transparent paper?

def parse_file(input_file: str) -> Tuple[Set[Tuple[int]], List[str]]:
    input_str = ''

    for line in open(input_file, 'r'):
        line = line.strip("")
        input_str += line

    dot_strings, folds = [input_line.split("\n") for input_line in input_str.split("\n\n")]

    dots = set()

    for dot_string in dot_strings:
        dots.add(tuple(int(coordinate) for coordinate in dot_string.split(",")))

    return dots, folds


if __name__ == '__main__':
    dots, folds = parse_file("test.csv")


    # answer_1 = output_numbers_sum
    # answer_2 = output_numbers_sum
    #
    # print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
