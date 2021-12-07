import csv
import numpy as np
from typing import List
import sys

sys.setrecursionlimit(10**6)


def parse_file(input_file: str) -> List[int]:
    all_initial_timers = []
    csv_reader = csv.reader(open(input_file, "r"))

    timer_strings = []

    for ts in csv_reader:
        timer_strings = ts

    for timer_string in timer_strings:
        all_initial_timers.append(int(timer_string))

    return all_initial_timers


def find_median_position(positions):
    n = len(positions)
    if n % 2 == 0:
        median = positions[n // 2]
    else:
        median1 = positions[n - 1 // 2]
        median2 = positions[n + 1 // 2]
        median = (median1 + median2) / 2

    return median


def fuel_expenditure(convergence_point, start_positions):
    fuel = sum([abs(start_position - convergence_point) for start_position in start_positions])
    return fuel


def exp_fuel_expenditure(convergence_point, start_positions):
    total_fuel = 0
    for convergence_distance in [abs(start_position - convergence_point) for start_position in start_positions]:
        fuel_per_distance = 0
        for i in range(int(convergence_distance)):
            fuel_per_distance += i+1
        total_fuel += fuel_per_distance

    return total_fuel


def find_convergence_point(positions, current_median):
    current_median_fuel = exp_fuel_expenditure(current_median, positions)

    if (current_median_fuel <= exp_fuel_expenditure(median - 1, positions) and
            (current_median_fuel <= exp_fuel_expenditure(median+1, positions))):
        convergence_point = current_median
        print("convergence is at ", convergence_point)
        return convergence_point

    else:
        if current_median_fuel > exp_fuel_expenditure(median - 1, positions):
            print("true convergence point is to the left")
            subsample = list(filter(lambda pos: [pos < median for pos in positions], positions))
            subsample_median = np.median(subsample)
        else:
            print("true convergence point is to the right")
            subsample = list(filter(lambda pos: [pos > median for pos in positions], positions))
            subsample_median = np.median(subsample)

        find_convergence_point(subsample, subsample_median)



if __name__ == '__main__':
    start_positions = parse_file("test2.csv")

    sorted_positions = sorted(start_positions)
    median = np.median(start_positions)
    convergence_point = np.median(start_positions)
    # exp_fuel_expenditure(convergence_point, start_positions)
    answer_1 = fuel_expenditure(convergence_point, start_positions)

    # exp_convergence_point = find_convergence_point(start_positions, median)
    answer_2 = find_convergence_point(start_positions, median)

    print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)
