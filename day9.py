# low points - the locations that are lower than any of its adjacent locations.
# Most locations have four adjacent locations (up, down, left, and right);
# locations on the edge or corner of the map have three or two adjacent locations, respectively.
# (Diagonal locations do not count as adjacent.)

# The risk level of a low point is 1 plus its height.

# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?


class Location:
    def __init__(self, up: int, down: int, left: int, right: int):
        self.up
        self.down
        self.left
        self.right

if __name__ == '__main__':
    # dots, folds = parse_file("input13.csv")

    # dots_after_first_fold = complete_fold(dots, folds[0])

    # answer_1 = len(dots_after_first_fold)

    # answer_2 = output_numbers_sum

    # print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)