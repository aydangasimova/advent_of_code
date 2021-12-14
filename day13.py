from typing import Tuple, Set, List, Dict


# How many dots are visible after completing just the first fold instruction on your transparent paper?

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
                distance_to_fold = dot[1]-fold[1]
                dots_after_fold.add((dot[0], fold[1]-distance_to_fold))
        elif fold[0] == 'x':
            if dot[0] > fold[1]:
                dots_to_remove.add(dot)
                distance_to_fold = dot[0] - fold[1]
                dots_after_fold.add((fold[1]-distance_to_fold, dot[1]))

    remaining_dots = dots_before_fold.difference(dots_to_remove)

    return dots_after_fold.union(remaining_dots)


def visualize_dots(dots_to_visualize, x_limit, y_limit):

    total_space = []

    for y in range(y_limit):
        total_space.append(["."]*(x_limit+1))

    for dot in dots_to_visualize:
        pass

    for line in total_space:
        print(line)

    for row_index, line in enumerate(total_space):
        for index in range(len(line)):
            if (index, row_index) in dots_to_visualize:
                print("#", end=" ")
            else:
                print(line[index], end=" ")
        print(" ")

# Finish folding the transparent paper according to the instructions.
# The manual says the code is always eight capital letters.
# What code do you use to activate the infrared thermal imaging camera system?

# Transformation = Callable[[DataFrame], DataFrame]

# def transform(df: DataFrame, *transformations: Transformation) -> DataFrame:
#     """
#     Performs all transformations on the input dataframe and returns the final result
#
#     Input:
#     - df:              A Spark DataFrame
#     - transformations: One or more transformation functions that accept a Spark
#             DataFrame as input and have a Spark DataFrame as output
#     """
#     for transformation in transformations:
#         df = transformation(df)
#     return df

# def transform_tables(airing: DataFrame, viewership: DataFrame, chunks: DataFrame) -> DataFrame:
#     return transform(
#         airing,
#         join_with_viewership(viewership=viewership),
#         join_with_chunks(chunks=chunks),
#     )

# def transform_tables(airing: DataFrame, viewership: DataFrame, chunks: DataFrame) -> DataFrame:
#     return transform(
#         airing,
#         join_with_viewership(viewership=viewership),
#         join_with_chunks(chunks=chunks),
#     )


if __name__ == '__main__':
    dots, folds = parse_file("test.csv")

    dots_after_first_fold = complete_fold(dots, folds[0])

    answer_1 = len(dots_after_first_fold)

    # for i, fold in enumerate(folds):
    #     complete_fold(complete_fold(folds[i+1]), folds[i])
    x_limit = max([dot[0] for dot in dots])
    y_limit = folds[0][1]

    visualize_dots(dots_after_first_fold, x_limit, y_limit)

    # answer_2 = output_numbers_sum
    #


    print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
