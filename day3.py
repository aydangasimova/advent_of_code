
def most_common_value_in_bit_position(bit_position, input_list):
    freq_1 = 0
    freq_0 = 0
    for row_ind in range(len(input_list)):
        if int(input_list[row_ind][bit_position]) == 1:
            freq_1 += 1
        else:
            freq_0 += 1

    if freq_1 > freq_0:
        return 1
    elif freq_1 < freq_0:
        return 0
    else:
        return 'equal'


def frequency_of_bits(input_file):
    """
    input is a diagnostic report - text file with binary numbers in each line

    Each bit in the gamma(epsilon) rate can be determined by finding the most(least) common bit
    in the corresponding position of all numbers in the diagnostic report.

    :returns the product of gamma and epsilon rates

    """
    input_list = [line.rstrip() for line in open(input_file, 'r')]

    gamma = ''
    epsilon = ''

    for bit_ind in range(len(input_list[0])):
        freq_1 = 0
        freq_0 = 0
        for row_ind in range(len(input_list)):
            if int(input_list[row_ind][bit_ind]) == 1:
                freq_1 += 1
            else:
                freq_0 += 1

        if freq_1 > freq_0:
            gamma += '1'
            epsilon += '0'
        elif freq_1 == freq_0:
            print('there are equal number of ones and zeros')
        else:
            gamma += '0'
            epsilon += '1'

    print('gamma is', gamma, 'epsilon is', epsilon)

    return int(gamma, 2)*int(epsilon, 2)


def verify_life_sup_rating():
    """
    The bit criteria depends on which type of rating value you want to find:

    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 1 in the position being considered.

    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 0 in the position being considered.

    Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
    If you only have one number left, stop; this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right.

    :return: life support rating which is a product of oxygen generator rating the CO2 scrubber rating
    """

    pass

if __name__ == '__main__':

    answer_1 = frequency_of_bits('input3.csv')
    # answer_2 = get_final_position_with_aim(input_df)

    print('Answer 1: ', answer_1)
          # 'Answer 2: ', answer_2)
