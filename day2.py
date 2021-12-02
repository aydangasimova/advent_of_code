import pandas as pd


def get_final_position(infput_df):
    """Calculates the horizontal position and depth you would have after following the planned course"""

    horizontal_p = infput_df['increase'][infput_df['direction'] == 'forward'].sum()
    depth_p = (infput_df['increase'][infput_df['direction'] == 'down'].sum() -
               infput_df['increase'][infput_df['direction'] == 'up'].sum())

    multiplied = horizontal_p*depth_p

    return multiplied


def get_final_position_alt(input_file):

    depth_p = 0
    horizontal_p = 0

    direction, increase = zip(*(line.split() for line in open(input_file, 'r')))

    print(direction)
    print(increase)
    for i in range(len(direction)):
        if direction[i] == 'forward':
            horizontal_p += int(increase[i])
        elif direction[i] == 'up':
            depth_p -= int(increase[i])
        else:
            depth_p += int(increase[i])

    return horizontal_p*depth_p


def get_final_position_with_aim(infput_df):
    """Calculates the horizontal position and depth you would have
        after following the planned course while adjusting aim"""

    aim = 0
    depth_p = 0
    horizontal_p = 0

    for index, row in infput_df.iterrows():
        if row['direction'] == 'down':
            aim += row['increase']
        elif row['direction'] == 'up':
            aim -= row['increase']
        else:
            depth_p += aim*row['increase']
            horizontal_p += row['increase']

    multiplied = horizontal_p * depth_p

    return multiplied


if __name__ == '__main__':
    input_df = pd.read_csv('input2.csv', names=['direction', 'increase'], delimiter=' ')

    answer_1 = get_final_position(input_df)
    answer_2 = get_final_position_with_aim(input_df)

    print('Answer 1: ', answer_1, 'Answer 2: ', answer_2)
