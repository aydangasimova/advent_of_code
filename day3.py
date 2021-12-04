
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

    gamma = ''
    epsilon = ''

    for bit_position in range(len(input_list[0])):
        if most_common_value_in_bit_position(bit_position, input_list) == 1:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print('gamma is', gamma, 'epsilon is', epsilon)

    return int(gamma, 2)*int(epsilon, 2)


def verify_life_sup_rating(input_list):
    """
    The bit criteria depends on which type of rating value you want to find:

    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 1 in the position being considered.

    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 0 in the position being considered.

    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 1 in the position being considered.

    Keep only numbers selected by the bit criteria for the type of rating value for which you are searching.
    Discard numbers which do not match the bit criteria. If you only have one number left, stop;
    this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right.

    :return: life support rating which is a product of oxygen generator rating the CO2 scrubber rating
    """
    fitting_oxygen_criteria = set(input_list)
    fitting_co2_criteria = set(input_list)

    oxygen_unfit = set()
    co2_unfit = set()

    for bit_position in range(len(input_list[0])):
        print(f"BIT POSITION {bit_position} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        mcv = most_common_value_in_bit_position(bit_position, input_list)

        for number in input_list:
            print(f"~~~~~~~~~~~~~~~~~~NUMBER IS {number}")

            if mcv == int(number[bit_position]):
                if len(co2_unfit) != 999:
                    print(f"MCV is {mcv} SAME AS {number[bit_position]}")
                    co2_unfit.add(number)
                    print(f"after  adding {number} len to CO2 unfit len is {len(co2_unfit)}")

            elif mcv == 'equal':
                # If 0 and 1 are equally common, keep values with a 1 in the position being considered.
                print(f'mcv is {mcv} should be equal')
                if int(number[bit_position]) == 1:
                    # print(f'number first digit is {int(number[bit_position])}, should be 1 therefore they need to go from CO2')
                    # print(f"len of CO2 fitting criteria is not yet 1, is {len(fitting_co2_criteria)}")
                    co2_unfit.add(number)
                    # print(f"after  removing {number} len of CO2 fitting criteria is {len(fitting_co2_criteria)}")

                else:
                    # print(f'number first digit is {int(number[0])}, should be 0 therefore they need to go from OXYGEN')
                    # print(f"len of OXYGEN fitting criteria is not yet 1, is {len(fitting_oxygen_criteria)}")
                    oxygen_unfit.add(number)
                    # print(f"after  removing {number} len of OXYGEN fitting criteria is {len(fitting_oxygen_criteria)}")
            else:
                if len(oxygen_unfit) != 999:
                    print(f"MCV is {mcv} DIFFERENT FROM {number[bit_position]} in position {bit_position}")
                    oxygen_unfit.add(number)
                    print(f"after  adding {number} len to OXYGEN unfit len is {len(oxygen_unfit)}")




    print(len(oxygen_unfit), len(co2_unfit), 'both should be 999')

    print(len(fitting_oxygen_criteria.difference(oxygen_unfit)), len(fitting_co2_criteria.difference(co2_unfit)), 'both should be 1')

    # add a stop once I find both
    oxygen_rating = next(iter(fitting_oxygen_criteria.difference(oxygen_unfit)))
    co2_rating = next(iter(fitting_co2_criteria.difference(co2_unfit)))
    print(oxygen_rating, co2_rating)

    return int(co2_rating, 2)*int(oxygen_rating, 2)


if __name__ == '__main__':

    input_list = [line.rstrip() for line in open('input3.csv', 'r')]
    # answer_1 = frequency_of_bits(input_list)
    answer_2 = verify_life_sup_rating(input_list)

    for i in range(len(input_list[0])):
        print(f" MCV in bit position {i} is {most_common_value_in_bit_position(i, input_list)}")

    # print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)
