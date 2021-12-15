from typing import Union, List

class Location:
    def __init__(
            self,
            height: int,
            row_index: int,
            position: int,
            up: Union[int, None],
            down: Union[int, None],
            left: Union[int, None],
            right: Union[int, None],
    ):
        self.height = height
        self.row_index = row_index
        self.position = position
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


class LocAlt:
    def __init__(
            self,
            row_index: int,
            position: int,
            all_lines: List[str],
    ):

        self.all_lines = all_lines
        self.height = int(self.all_lines[row_index][position])
        self.row_index = row_index
        self.position = position

    def get_up_loc(self):
        row_up = self.row_index - 1
        position_up = self.position

        if row_up < 0:
            self.up_height = None
            return None
        else:
            self.up_height = int(self.all_lines[row_up][position_up])
            return LocAlt(row_up, position_up, self.all_lines)

    def get_down_loc(self):
        row_down = self.row_index + 1
        position_down = self.position

        if row_down > len(self.all_lines) - 1:
            self.down_height = None
            return None
        else:
            self.down_height = int(self.all_lines[row_down][position_down])
            return LocAlt(row_down, position_down, self.all_lines)

    def get_left_loc(self):
        row_left = self.row_index
        position_left = self.position - 1

        if position_left < 0:
            self.left_height = None
            return None
        else:
            self.left_height = int(self.all_lines[row_left][position_left])
            return LocAlt(row_left, position_left, self.all_lines)

    def get_right_loc(self):
        row_right = self.row_index
        position_right = self.position + 1

        if position_right > len(self.all_lines) - 1:
            self.right_height = None
            return None
        else:
            self.right_height = int(self.all_lines[row_right][position_right])
            return LocAlt(row_right, position_right, self.all_lines)

    def is_low_point(self, adjacent_list) -> bool:
        no_null_adjacent_list = list(filter(lambda nb: (nb is not None), adjacent_list))
        if self.height < min([nb.height for nb in no_null_adjacent_list]):
            return True

    def is_high_point(self, adjacent_list) -> bool:
        no_null_adjacent_list = list(filter(lambda nb: (nb is not None), adjacent_list))
        if self.height > max([nb.height for nb in no_null_adjacent_list]) and not 9:
            return True

    def get_risk_level(self) -> int:
        return self.height + 1


class BasinLocation(LocAlt):

    def __init__(self, basin_low_point: LocAlt, all_locations: List[LocAlt], row_index: int, position: int,
                 all_lines: List[str]):

        super().__init__(row_index, position, all_lines)
        self.basin_low_point = basin_low_point
        self.all_locations = all_locations
        self.row_index = row_index
        self.position = position

        self.basin_edge_locs = [self.get_up_loc(),
                                self.get_left_loc(),
                                self.get_right_loc(),
                                self.get_down_loc()]
        self.basin_complete = False
        self.no_null_edges = list(filter(lambda nb: (nb is not None), self.basin_edge_locs))
        self.basin_locations = [self] + [edge for edge in self.no_null_edges]
        self.basin_size = len(self.basin_locations)

    def update_no_null_edges(self):
        self.no_null_edges = list(filter(lambda nb: (nb is not None), self.basin_edge_locs))

    def update_basin_edges(self):
        new_edges = []
        for edge in self.no_null_edges:
            edge_adjacent_list = [edge.get_right_loc(),
                                  edge.get_down_loc(),
                                  edge.get_left_loc(),
                                  edge.get_up_loc()]
            if edge.is_high_point(edge_adjacent_list):
                self.basin_complete = True
                break
            else:
                for potential_edge in filter(
                        lambda potential_edge: ((potential_edge.height > edge.height) and (potential_edge != 9)),
                        edge_adjacent_list):
                    if potential_edge not in self.basin_locations:
                        new_edges.append(potential_edge)

                        self.basin_locations.append(potential_edge)
                        self.basin_edge_locs.append(potential_edge)
                        self.basin_edge_locs.remove(edge)
                        self.update_no_null_edges()

#
# def parse_file(input_file: str) -> List[Location]:
#     locations = []
#
#     all_lines = [line.strip() for line in open(input_file, 'r').readlines()]
#
#     for row_number, line in enumerate(all_lines):
#         line = line.strip("")
#         for position, number in enumerate(line):
#             # print(f"looking at number {number} in position {position} and row {row_number} line {line}")
#
#             #  There is no upper neighbour
#             up = None if row_number == 0 else int(all_lines[row_number - 1][position])
#             #  There is no bottom neighbour
#             down = None if row_number == len(all_lines) - 1 else int(all_lines[row_number + 1][position])
#             # There is no left neighbour (it's an upper left corner)
#             left = None if position == 0 else int(line[position - 1])
#             # There is no right neighbour (it's an upper right corner)
#             right = None if position == len(line) - 1 else int(line[position + 1])
#
#             location = Location(int(number),
#                                 row_index=row_number,
#                                 position=position,
#                                 up=up,
#                                 down=down,
#                                 left=left,
#                                 right=right)
#
#             locations.append(location)
#             # print(f"added a new location for {number} in line {line}")
#
#     return locations


# A basin is all locations that eventually flow downward to a single low point.
# Therefore, every low point has a basin, although some basins are very small.
# Locations of height 9 do not count as being in any basin,
# and all other locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point.
# The example above has four basins.

# What do you get if you multiply together the sizes of the three largest basins?

if __name__ == '__main__':
    #
    # locations = parse_file("input9.csv")
    #
    # low_points = []
    # risk_level_sum = 0
    #
    # for location in locations:
    #     if location.is_low_point():
    #         low_points.append(location)
    #         risk_level_sum += location.get_risk_level()
    #
    #
    all_lines = [line.strip() for line in open("test9.csv", 'r').readlines()]

    locations = []
    low_points = []
    risk_level_sum = 0
    for row_number, row in enumerate(all_lines):
        for position in range(len(row)):
            loc = LocAlt(row_index=row_number, position=position, all_lines=all_lines)
            locations.append(loc)
            adjacent_locations = [loc.get_up_loc(), loc.get_left_loc(), loc.get_down_loc(), loc.get_right_loc()]
            if loc.is_low_point(adjacent_locations):
                low_points.append(loc)
                risk_level_sum += loc.get_risk_level()

    answer_1 = risk_level_sum

    all_basins = []
    for low_point in low_points:
        basin = BasinLocation(basin_low_point=low_point,
                              all_locations=locations,
                              row_index=low_point.row_index,
                              position=low_point.position,
                              all_lines=all_lines)

        if not basin.basin_complete:
            basin.update_basin_edges()
        else:
            all_basins.append(basin)

    three_largest_basins = sorted([basin.basin_size for basin in all_basins], reverse=True)[:3]

    product = 1
    for basin_size in three_largest_basins:
        product = product*basin_size

    answer_2 = product

    print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)
