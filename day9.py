# low points - the locations that are lower than any of its adjacent locations.
# Most locations have four adjacent locations (up, down, left, and right);
# locations on the edge or corner of the map have three or two adjacent locations, respectively.
# (Diagonal locations do not count as adjacent.)

# The risk level of a low point is 1 plus its height.

# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
from typing import Union, List


class Location:
    def __init__(
            self,
            height: int,
            up: Union[int, None],
            down: Union[int, None],
            left: Union[int, None],
            right: Union[int, None]):

        self.height = height
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.adjacent_list = [self.up, self.down, self.right, self.left]

    def is_low_point(self) -> bool:
        no_null_adjacent_list = list(filter(lambda nb: (nb is not None), self.adjacent_list))
        if self.height < min(no_null_adjacent_list):
            return True

    def get_risk_level(self) -> int:
        return self.height + 1


def parse_file(input_file: str) -> List[Location]:
    locations = []

    all_lines = [line.strip() for line in open(input_file, 'r').readlines()]

    for row_number, line in enumerate(all_lines):
        line = line.strip("")
        for position, number in enumerate(line):
            # print(f"looking at number {number} in position {position} and row {row_number} line {line}")

            #  There is no upper neighbour
            up = None if row_number == 0 else int(all_lines[row_number-1][position])
            #  There is no bottom neighbour
            down = None if row_number == len(all_lines)-1 else int(all_lines[row_number + 1][position])
            # There is no left neighbour (it's an upper left corner)
            left = None if position == 0 else int(line[position - 1])
            # There is no right neighbour (it's an upper right corner)
            right = None if position == len(line)-1 else int(line[position+1])

            location = Location(int(number),
                                up=up,
                                down=down,
                                left=left,
                                right=right)

            locations.append(location)
            # print(f"added a new location for {number} in line {line}")

    return locations


if __name__ == '__main__':

    locations = parse_file("input9.csv")

    low_points = []
    risk_level_sum = 0

    for location in locations:
        if location.is_low_point():
            low_points.append(location)
            risk_level_sum += location.get_risk_level()

    answer_1 = risk_level_sum

    # answer_2 = output_numbers_sum

    print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)