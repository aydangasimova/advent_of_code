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


class School:
    def __init__(self, all_initial_timers, spawn_rate=6, newborn_spawn_rate=9):
        self.all_initial_timers = all_initial_timers
        self.spawn_rate = spawn_rate
        self.current_timers = all_initial_timers
        self.school_size = len(all_initial_timers)
        self.newborn_spawn_rate = newborn_spawn_rate

    def make_fish_babies(self, newborn_spawn_rate=9):
        baby_fishies = Fish(newborn_spawn_rate)
        self.current_timers.append(baby_fishies)

    def update_timers(self):
        # reset timer to count down again and make a new fish with internal_timer range(0, 9)
        # next day new fish starts counting down too

        reset_fishies = list(filter(lambda timer: timer != 0, self.current_timers))
        count_new_babies = self.school_size - len(reset_fishies)
        self.current_timers = [reset_fish_timer - 1 for reset_fish_timer in reset_fishies]

        if count_new_babies > 0:
            self.current_timers += [self.newborn_spawn_rate]*count_new_babies

        self.school_size += count_new_babies


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


def simulate_faster(all_initial_timers: List, days_to_run: int = 256):
    school = School(all_initial_timers, days_to_run)
    days_past = 0
    while days_to_run - days_past > 0:
        days_past += 1
        school.update_timers()

    return school.school_size


if __name__ == '__main__':

    all_initial_timers = parse_file("test.csv")

    # answer_1 = simulate(all_initial_timers)
    answer_2 = simulate_faster(all_initial_timers, days_to_run=256)

    # print('Answer 1: ', answer_1)

    # 26984457539 test answer
    #  my answer
    print('Answer 2: ', answer_2)
