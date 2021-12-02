import pandas as pd


def count_higher_than_previous(input_data):
    """Calculates how many of the measurements in a dataset are higher than the previous"""
    measurements = pd.read_csv(input_data, header=None)
    higher_than_previous = 0

    for i in range(1, len(measurements)):
        if measurements.iloc[i][0] > measurements.iloc[i - 1][0]:
            higher_than_previous += 1

    return higher_than_previous


def count_sliding_window_increases(input_data):
    """Counts the number of times the sum of measurements in this sliding window increases from the previous sum"""
    measurements = pd.read_csv(input_data, header=None)

    higher_window_counts = 0
    for i in range(0, len(measurements)-3):
        current_window_sum = 0
        next_window_sum = 0
        for j in range(i, i+3):
            current_window_sum += measurements.iloc[j][0]
            next_window_sum += measurements.iloc[j+1][0]
        if current_window_sum < next_window_sum:
            higher_window_counts += 1

    return higher_window_counts


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer_1 = count_higher_than_previous('input.csv')
    answer_2 = count_sliding_window_increases('input.csv')

    print('Answer 1: ', answer_1, 'Answer 2: ', answer_2)
