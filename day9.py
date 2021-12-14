from typing import Union, List


class Location:
    def __init__(
            self,
            height: int,
            row_index: int,
            line_index: int,
            up: Union[int, None],
            down: Union[int, None],
            left: Union[int, None],
            right: Union[int, None]):

        self.height = height
        self.row_index = row_index
        self.line_index = line_index
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


class BasinLocation(Location):

    def __init__(self,
                 basin_low_point: Location,
                 row_index,
                 line_index,
                 height: int,
                 up: Union[int, None],
                 down: Union[int, None],
                 left: Union[int, None],
                 right: Union[int, None]):

        super().__init__(height, row_index, line_index, up, down, left, right)

        self.basin_low_point = basin_low_point
        self.basin_id = str(row_index) + str(line_index)
        self.basin_locations = []
        self.basin_size = len(self.basin_locations)
        self.basin_edges: list[Location] = []
        self.basin_complete = False

    def add_to_basin(self, new_basin_location: Location):
        self.basin_locations.append(new_basin_location)


    def update_basin_edges(self):
        new_edges = []
        for edge in self.basin_edges:
            no_null_adjacent_list = list(filter(lambda nb: (nb is not None), self.adjacent_list))
            if all(potential_edge < edge.height for potential_edge in no_null_adjacent_list):
                self.basin_complete = True
            else:
                for potential_edge in filter(lambda potential_edge: ((potential_edge>edge.height) and (potential_edge!=9)), no_null_adjacent_list):
                    # new_edge = Location(potential_edge, )
                    # new_edges.append(new_edge)
                    pass




#     if there is no more need to update basin edges


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
                                row_index=row_number,
                                line_index=position,
                                up=up,
                                down=down,
                                left=left,
                                right=right)

            locations.append(location)
            # print(f"added a new location for {number} in line {line}")

    return locations


# A basin is all locations that eventually flow downward to a single low point.
# Therefore, every low point has a basin, although some basins are very small.
# Locations of height 9 do not count as being in any basin,
# and all other locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point.
# The example above has four basins.

# What do you get if you multiply together the sizes of the three largest basins?

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