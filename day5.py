# At how many points do at least two lines overlap? Only consider horizontal and vertical lines




if __name__ == '__main__':

    input_list = [line.rstrip() for line in open('test.csv', 'r')]
    line_list = []
    line_end_list = []

    for line in input_list:
        line_ends = line.split(' -> ')
        print(line_ends)
        # for line_end in line_ends:
        #     line_end_list.append([tuple(map(int, line_end.split(',')))])

    print(line_end_list)
    # answer_1 = frequency_of_bits(input_list)
    # answer_2 = verify_life_sup_rating(input_list)

    # print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
