import csv
from typing import List, Dict


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
    def __init__(self, initial_timer, school, spawn_rate=6):
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
    def __init__(self, all_initial_timers, spawn_rate=6, newborn_spawn_rate=8):
        self.all_initial_timers = all_initial_timers
        self.spawn_rate = spawn_rate
        self.school_size = len(all_initial_timers)
        self.newborn_spawn_rate = newborn_spawn_rate

        self.current_timers: Dict[int, int] = {}
        for timer in self.all_initial_timers:
            if timer in self.current_timers.keys():
                self.current_timers[timer] += 1
            else:
                self.current_timers[timer] = 1

    def update_timers(self):
        count_new_babies = 0

        new_timers = {}
        for timer in sorted(self.current_timers.keys()):
            if timer != 0:
                if timer-1 in new_timers.keys():
                    new_timers[timer-1] += self.current_timers[timer]
                else:
                    new_timers[timer-1] = self.current_timers[timer]


            else:
                count_new_babies = self.current_timers[0]
                if count_new_babies > 0:
                    new_timers[self.newborn_spawn_rate] = count_new_babies
                    if self.spawn_rate in new_timers:
                        new_timers[self.spawn_rate] += count_new_babies
                    else:
                        new_timers[self.spawn_rate] = count_new_babies

        self.current_timers = new_timers
        self.school_size += count_new_babies


def simulate_faster(all_initial_timers: List, days_to_run: int = 256):

    school = School(all_initial_timers)
    days_past = 0

    while days_to_run - days_past > 0:
        days_past += 1
        school.update_timers()

    return school.school_size


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

    answer_1 = simulate(all_initial_timers)
    answer_2 = simulate_faster(all_initial_timers, days_to_run=256)

    print('Answer 1: ', answer_1)
    print('Answer 2: ', answer_2)
