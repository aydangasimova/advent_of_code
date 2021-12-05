from typing import List, Dict, Tuple


def calculate_win_score(board_rows: List[List[int]], called_numbers, winning_number) -> int:

    all_board_numbers = [number for row in board_rows for number in row]
    all_unmarked_numbers = list(set(all_board_numbers) - set(called_numbers))
    score = sum(all_unmarked_numbers)*winning_number

    return score


def get_list_of_numbers_to_call(input_csv: str) -> List:
    first_line = [line.rstrip() for line in open(input_csv, 'r')][0]
    numbers_to_call = list(map(int, first_line.split(',')))
    return numbers_to_call


def parse_boards(input_csv: str) -> Dict[int, List[List[int]]]:
    all_boards: Dict = {}

    input = [line.rstrip() for line in open(input_csv, 'r')][2:]
    board_id = 0
    all_boards[board_id] = []

    for line in input:
        if line == '':
            board_id += 1
            all_boards[board_id] = []
        else:
            # print(line)
            all_boards[board_id].append(list(map(int, line.split())))

    return all_boards


def check_for_full_row(board, called_numbers) -> bool:
    for row in board[1]:
        if all(number in called_numbers for number in row) is True:
            result = True
            break
        else:
            result = False
    return result


def check_for_full_col(board, called_numbers) -> bool:

    columns = []
    for col_index in range(len(board[1])):
        column = []
        for row in board[1]:
            column.append(row[col_index])
        columns.append(column)

    for col in columns:
        if all(number in called_numbers for number in col) is True:
            result = True
            break
        else:
            result = False

    return result


if __name__ == '__main__':

    numbers_to_call = get_list_of_numbers_to_call("input4.csv")
    all_boards = parse_boards("input4.csv")
    called_numbers = []
    winning_board: Tuple[int, List[List[int]]]
    winner = False

    for number in numbers_to_call:
        called_numbers.append(number)
        if winner is False:
            for board in all_boards.items():
                if check_for_full_row(board, called_numbers) or check_for_full_col(board, called_numbers):
                    winner = True
                    winning_board = board
                    winning_number = number
                    # print("we have a winner", winning_board)
                    break
        else:
            break

    answer_1 = calculate_win_score(board_rows=winning_board[1],
                                   called_numbers=called_numbers,
                                   winning_number=winning_number)

    # figure out which board will win last
    called_numbers = []

    winners_in_order = {}
    winning_boards_with_number = {}
    winning_boards = []

    for index, number in enumerate(numbers_to_call):
        called_numbers.append(number)

        for board in all_boards.items():
            if board not in winning_boards:
                if check_for_full_row(board, called_numbers) != check_for_full_col(board, called_numbers):
                    winning_boards.append(board)
                    winners_in_order[index] = (number, board[0])

    last_winner = sorted(winners_in_order.items(), reverse=True)[0]
    last_winner_board = all_boards[last_winner[1][1]]
    last_winning_number = last_winner[1][0]

    answer_2 = calculate_win_score(board_rows=last_winner_board,
                                   called_numbers=numbers_to_call[:last_winner[0]+1],
                                   winning_number=last_winning_number)

    print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)
