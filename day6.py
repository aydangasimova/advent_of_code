import csv
from typing import List


def parse_file(input_file: str) -> List[int]:
    all_initial_timers = []
    csv_reader = csv.reader(open(input_file, "r"))

    timer_strings = []

    for ts in csv_reader:
        timer_strings = ts

    for timer_string in timer_strings:
        all_initial_timers.append(int(timer_string))

    return all_initial_timers


class Fish:
    def __init__(self, initial_timer, school: List, spawn_rate=6):
        self.initial_timer = initial_timer
        self.spawn_rate = spawn_rate
        self.current_timer = initial_timer
        self.school = school

    def make_fish_baby(self, newborn_spawn_rate=9):
        baby_fish = Fish(newborn_spawn_rate, self.school)
        self.school.append(baby_fish)

    def update_timer(self):
        # reset timer to count down again and make a new fish with internal_timer range(0, 9)
        # next day new fish starts counting down too
        if self.current_timer != 0:
            self.current_timer = self.current_timer - 1
        elif self.current_timer == 0:
            self.current_timer = self.spawn_rate
            self.make_fish_baby()


def simulate(all_initial_timers: List, days_to_run: int = 80):

    school = []
    for initial_timer in all_initial_timers:
        school.append(Fish(initial_timer, school))

    days_past = 0
    while days_to_run - days_past > 0:
        days_past += 1
        for fish in school:
            fish.update_timer()

    return len(school)


if __name__ == '__main__':

    all_initial_timers = parse_file("input6.csv")

    # reset timer to count down again and make a new fish with internal_timer range(0, 9)
    # next day new fish starts counting down too

    answer_1 = simulate(all_initial_timers)
    # answer_2 =

    print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
