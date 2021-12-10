# PART 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?

# For each entry, determine all of the wire/segment connections and decode the four-digit output values.
# What do you get if you add up all of the output values?
from typing import List


class Digit:
    def __init__(self, digit: int):
        self.digit_name_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                                 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

        self.digit_letters_dict = {0: {'a', 'b', 'c', 'f', 'g'},
                                   1: {'c', 'f'},
                                   2: {'a', 'c', 'd', 'e', 'g'},
                                   3: {'a', 'c', 'd', 'f', 'g'},
                                   4: {'b', 'd', 'c', 'f'},
                                   5: {'a', 'b', 'd', 'f', 'g'},
                                   6: {'a', 'b', 'd', 'e', 'f', 'g'},
                                   7: {'a', 'c', 'f'},
                                   8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                                   9: {'a', 'b', 'c', 'd', 'f', 'g'}}

        self.digit = digit
        self.digit_name = self.digit_name_dict[digit]

        self.letters_in_digit = self.digit_letters_dict[self.digit]
        self.letter_count_in_number = len(self.letters_in_digit)


class Display:
    def __init__(self, displayed_string: str):
        self.displayed_string = displayed_string

    def translator(self):
        pass


class Decoder:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.correct_letter_dict = {0: {'a', 'b', 'c', 'f', 'g'},
                                    1: {'c', 'f'},
                                    2: {'a', 'c', 'd', 'e', 'g'},
                                    3: {'a', 'c', 'd', 'f', 'g'},
                                    4: {'b', 'd', 'c', 'f'},
                                    5: {'a', 'b', 'd', 'f', 'g'},
                                    6: {'a', 'b', 'd', 'e', 'f', 'g'},
                                    7: {'a', 'c', 'f'},
                                    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                                    9: {'a', 'b', 'c', 'd', 'f', 'g'}}
        self.decoder_dict = {}
        self.letter_dict = {}
        self.unsolved_letters = []
        self.letter_translator = {}

    def add_digit_to_decoder_dict(self, digit, encoded_letters):
        self.decoder_dict[digit] = encoded_letters

    def add_to_letter_dict(self, digit, encoded_letters):
        for letter in encoded_letters:
            pass
        return 0

    def get_letter_frequency(self):
        for letter in puzzle[0]:
            pass

    def add_to_letter_translator(self, encoded_letter_string, actual_letter):
        self.letter_tranlator[actual_letter] = encoded_letter_string


def find_easy_encoded_digits(easy_digits, all_puzzles):

    easy_occurrence = 0
    for puzzle in all_puzzles:
        for encoded_digit in puzzle[1]:
            for digit in easy_digits:
                if len(encoded_digit) == Digit(digit).letter_count_in_number:
                    easy_occurrence += 1
    return easy_occurrence


def parse_file(input_file: str) -> List[List[List[str]]]:

    all_puzzles = []
    with open(input_file, 'r') as file:
        all_lines = [[st for st in line.split()] for line in file]
        for line in all_lines:
            signal_patterns = line[:10]
            encoded_output = line[11:]
            all_puzzles.append([signal_patterns, encoded_output])

    return all_puzzles


def get_letter_frequency(letter_list):
    letter_frequency = {}
    for letters in letter_list:
        for letter in letters:
            if letter in letter_frequency.keys():
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1

    return letter_frequency


if __name__ == '__main__':

    correct_letter_dict = {0: {'a', 'b', 'c', 'f', 'g'},
                           1: {'c', 'f'},
                           2: {'a', 'c', 'd', 'e', 'g'},
                           3: {'a', 'c', 'd', 'f', 'g'},
                           4: {'b', 'd', 'c', 'f'},
                           5: {'a', 'b', 'd', 'f', 'g'},
                           6: {'a', 'b', 'd', 'e', 'f', 'g'},
                           7: {'a', 'c', 'f'},
                           8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                           9: {'a', 'b', 'c', 'd', 'f', 'g'}}

    all_puzzles = parse_file("test.csv")

    all_digits = {d for d in range(0,10)}
    easy_digits = {1, 4, 7, 8}
    hard_digits = all_digits.difference(easy_digits)

    answer_1 = find_easy_encoded_digits(easy_digits, all_puzzles)

    correct_letter_freq = get_letter_frequency(correct_letter_dict.values())

    for puzzle in all_puzzles:
        signal_patterns = puzzle[0]
        encoded_output = puzzle[1]
        encoded_letter_freq = get_letter_frequency(signal_patterns)
        decoder = Decoder(puzzle)

        for signal_pattern in signal_patterns:
            for easy_digit in easy_digits:

                if len(signal_pattern) == Digit(easy_digit).letter_count_in_number:
                    decoder.add_digit_to_decoder_dict(easy_digit, signal_pattern)
                # if you know that 1 is "cf" and 7 is "acf" => get that up_horizontal_line = ~a~ => deduce up_horizontal_line in 8
                # you know ~a~ based on difference between 1 and 7
                decoder.letter_translator["a"] = decoder.decoder_dict[7].difference(decoder.decoder_dict[1])

            for actual_letter in correct_letter_freq.items():
                for encoded_letter in encoded_letter_freq.items():
                    if encoded_letter[1] in [6, 3, 9]:
                        # knowing {'c': 8, 'a': 8, 'b': 6, 'g': 7, 'f': 9, 'd': 7, 'e': 3},
                        # you know ~b~ is the only one with 6 mentions
                        # you know ~e~ is the only one with 3 mentions
                        # you know ~f~ is the only one with 9 mentions
                        if encoded_letter[1] == actual_letter[1]:
                            decoder.letter_translator[actual_letter[0]] = encoded_letter[0]
                        elif (encoded_letter[1] == 8) and (encoded_letter[1] != 'a'):
                            # knowing ~a~ you can deduce that ~c~ is the only other letter with 8
                            decoder.letter_translator['c'] = encoded_letter[0]

            # knowing which letter is 4 and which letters are 'bcf' you can deduce what ~d~
            bcf = set([decoder.letter_translator[bcf] for bcf in ['b', 'c', 'f']])
            decoder.letter_translator['d'] = decoder.decoder_dict[4].difference(bcf)

            # knowing ~d~ you know the remaining letter (with 7 freq) is ~g~
            for actual_letter in correct_letter_freq.items():
                for encoded_letter in encoded_letter_freq.items():
                    if (encoded_letter[1] == 7) and (encoded_letter[1] != 'd'):
                        decoder.letter_translator['g'] = encoded_letter[0]

        print(decoder.decoder_dict)
        print(encoded_letter_freq)





    # answer_2 = simulate_faster(all_initial_timers, days_to_run=256)

    print('Answer 1: ', answer_1)
    # print('Answer 2: ', answer_2)
