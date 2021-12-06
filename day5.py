# At how many points do at least two lines overlap? Only consider horizontal and vertical lines

def parse_file(input_file):
    line_tuple_list = []

    for line in [line.rstrip() for line in open(input_file, 'r')]:
        str_line_ends = line.split(' -> ')
        int_line_ends = []
        for line_end in str_line_ends:
            int_line_ends.append(tuple(map(int, line_end.split(','))))

        line_tuple_list.append(int_line_ends)
    return line_tuple_list


def count_crossed_points(horizontal_lines, vertical_lines, diagonal_lines=None):

    point_cross_dict = {}

    for line in horizontal_lines:
        y_value = line[0][1]
        x_range = sorted([line[0][0], line[1][0]])

        for x_value in range(x_range[0], x_range[1]+1):
            point = (x_value, y_value)
            if point in point_cross_dict.keys():
                point_cross_dict[point] += 1
            else:
                point_cross_dict[point] = 1

    for line in vertical_lines:
        x_value = line[0][0]
        y_range = sorted([line[0][1], line[1][1]])

        for y_value in range(y_range[0], y_range[1] + 1):
            point = (x_value, y_value)
            if point in point_cross_dict.keys():
                point_cross_dict[point] += 1
            else:
                point_cross_dict[point] = 1

    if diagonal_lines:
        for i, line in enumerate(diagonal_lines):
            x_unsorted =[line[0][0], line[1][0]]
            x_range = sorted(x_unsorted)

            y_unsorted = [line[0][1], line[1][1]]
            y_range = sorted(y_unsorted)
            print(f"looking at line {line}, with x range of {x_range}")
            print(f"and y range of {y_range}")

            for x_value, y_value in zip(range(x_range[0], x_range[1]+1), range(y_range[0], y_range[1]+1)):
                point = (x_value, y_value)
                print(f"point is {point}")
                if point in point_cross_dict.keys():
                    point_cross_dict[point] += 1
                else:
                    point_cross_dict[point] = 1

    return point_cross_dict


def count_overlap_points(point_cross_dict):
    count = 0
    for point in point_cross_dict:
        if point_cross_dict[point] >= 2:
            count += 1
    return count


if __name__ == '__main__':

    line_tuple_list = parse_file('test.csv')
    horizontal_lines = []
    vertical_lines = []

    for line in line_tuple_list:
        if line[0][1] == line[1][1]:
            horizontal_lines.append(line)

        if line[0][0] == line[1][0]:
            vertical_lines.append(line)

    point_cross_dict1 = count_crossed_points(horizontal_lines, vertical_lines)

    answer_1 = count_overlap_points(point_cross_dict1)

    non_horizontal = list(filter(lambda line: line not in horizontal_lines, line_tuple_list))
    diagonal_lines = list(filter(lambda line: line not in vertical_lines, non_horizontal))

    point_cross_dict2 = count_crossed_points(horizontal_lines, vertical_lines, diagonal_lines)
    answer_2 = count_overlap_points(point_cross_dict2)

    print(diagonal_lines)

    print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)