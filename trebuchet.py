import os
import re

#Read the input text and get all the calibration values into an array
with open("./input.txt") as f:
    calibration_doc = f.read()

calibration_values = calibration_doc.split("\n")

global number_helper_dict
number_helper_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }


def find_all_numbers(word:str) -> str:

    digits = []

    for i, char in enumerate(word):
        if not char.isalpha():
            digits.append(char)

        for number in number_helper_dict.keys():
        
            if word[i:].startswith(number):
                digits.append(str(number_helper_dict.get(number)))

    return digits



"""Define mapping function to get the first and last digit in a string"""
def get_first_last_digit(text: str) -> int: 

    #Get the integer numbers for word representations in text and all digits
    digits = find_all_numbers(text)
    
    first_last_digit = digits[0] + digits[len(digits)-1]
    return int(first_last_digit)


calibration_sum = sum(map(get_first_last_digit, calibration_values))

print(calibration_sum)