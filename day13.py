from typing import Tuple, Set, Dict


def parse_file(input_file: str) -> Tuple[Set[Tuple[int]], Dict[int, Tuple[str, int]]]:
    input_str = ''

    for line in open(input_file, 'r'):
        line = line.strip("")
        input_str += line

    dot_strings, fold_strings = [input_line.split("\n") for input_line in input_str.split("\n\n")]

    folds = {}

    for i, fold_string in enumerate(fold_strings):
        folds[i] = (fold_string[11], int(fold_string[13:]))

    dots = set()
    for dot_string in dot_strings:
        dots.add(tuple(int(coordinate) for coordinate in dot_string.split(",")))

    return dots, folds


def complete_fold(dots_before_fold: Set, fold: Tuple[str, int]) -> Set:
    dots_after_fold = set()
    dots_to_remove = set()

    for dot in dots_before_fold:
        if fold[0] == 'y':
            # for all dots, if dot is beyond/down/higher than 'y',
            # reverse them by reducing y value with fold line - distance of y to fold
            if dot[1] > fold[1]:
                dots_to_remove.add(dot)
                distance_to_fold = dot[1] - fold[1]
                dots_after_fold.add((dot[0], fold[1] - distance_to_fold))
        elif fold[0] == 'x':
            if dot[0] > fold[1]:
                dots_to_remove.add(dot)
                distance_to_fold = dot[0] - fold[1]
                dots_after_fold.add((fold[1] - distance_to_fold, dot[1]))

    remaining_dots = dots_before_fold.difference(dots_to_remove)

    return dots_after_fold.union(remaining_dots)


def visualize_dots(dots_to_visualize, x_limit, y_limit):
    total_space = []

    for y in range(y_limit):
        total_space.append(["."] * (x_limit + 1))

    for line in total_space:
        print(line)

    for row_index, line in enumerate(total_space):
        for index in range(len(line)):
            if (index, row_index) in dots_to_visualize:
                print("#", end=" ")
            else:
                print(line[index], end=" ")
        print(" ")


if __name__ == '__main__':
    dots, folds = parse_file("input13.csv")

    dots_after_first_fold = complete_fold(dots, folds[0])

    answer_1 = len(dots_after_first_fold)

    x_limit = max([dot[0] for dot in dots])
    y_limit = folds[0][1]

    visualize_dots(dots_after_first_fold, x_limit, y_limit)

    fold_dot_outcome = {}

    for fold_id, fold in folds.items():
        if fold_id == 0:
            fold_dot_outcome[fold_id] = complete_fold(dots, fold)
        else:
            fold_dot_outcome[fold_id] = complete_fold(fold_dot_outcome[fold_id - 1], fold)

    final_dots = fold_dot_outcome[list(folds.keys())[-1]]

    y_limit_found = False
    x_limit_found = False
    for i in range(1, len(folds.keys())):
        if folds[len(folds.keys()) - i][0] == "y":
            if not y_limit_found:
                y_limit = folds[len(folds.keys()) - i][1]
                y_limit_found = True
                break
        elif folds[len(folds.keys()) - i][0] == "x":
            if not x_limit_found:
                x_limit = folds[len(folds.keys()) - i][1]
                x_limit_found = True
                break

    print(f"x lim is {x_limit}")
    print(f"y lim is {y_limit}")

    visualize_dots(final_dots, x_limit, y_limit)

    answer_2 = "EFJKZLBL"

    print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)
