from typing import List, Dict

import pandas as pd


class Board:
    def __init__(self, line_list, board_id):
        self.board_id = board_id
        self.board = line_list

    def update_board(self, called_number: int):
        pass

    def sum_board_column(self) -> int:
        pass

    def sum_board_row(self) -> int:
        pass


def calculate_win_score(board: pd.DataFrame) -> int:
    pass


def get_list_of_numbers_to_call(input_csv: str) -> List:
    first_line = [line.rstrip() for line in open(input_csv, 'r')][0]
    numbers_to_call = list(map(int, first_line.split(',')))
    return numbers_to_call


def parse_boards(input_csv: str) -> Dict[int, List[List[int]]]:
    all_boards: Dict = {}

    input = [line.rstrip() for line in open("input4.csv", 'r')][2:]
    board_id = 0
    all_boards[board_id] = []

    for line in input:
        if line == '':
            board_id += 1
            all_boards[board_id] = []
        else:
            print(line)
            all_boards[board_id].append(list(map(int, line.split())))

    return all_boards


def call_number(called_number: int, boards: List) -> List:
    pass


if __name__ == '__main__':

    # TODO call number until there is a winner, identify winning board and calculate its score
    called_numbers = get_list_of_numbers_to_call("input4.csv")
    print(f"The following numbers are called, {called_numbers}")


    # answer_1 = frequency_of_bits(input_list)
    # answer_2 = verify_life_sup_rating(input_list)

    # print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
