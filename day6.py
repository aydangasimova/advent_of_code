import csv
from typing import List


class simulate:
    def __init__(self, all_initial_timers: List):
        self.all_initial_timers = all_initial_timers

    def day_pass(self):

        self.current_timers=
        return self.current_timers()

if __name__ == '__main__':

    file = open("input6.csv", "r")
    csv_reader = csv.reader(file)
    print(csv_reader)

    for i in csv_reader:

    # all_initial_timers = []
    # for num in csv_reader:
    #     all_initial_timers.append(num)

    all_initial_timers = []
    for line in open("input6.csv", 'r'):
        print(type(line))
        for timer in line.rstrip(" , "):
            print(timer)
            # all_initial_timers.append(timer)


    print(all_initial_timers)

    spawn_rate = 7
    days_to_spawn = 7

    # time down
    internal_timer = range(0, 7)
    # reset timer to count down again and make a new fish with internal_timer range(0, 9)
    # next day new fish starts counting down too

    # answer_1 =
    # answer_2 =

    # print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
