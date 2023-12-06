import os

#Read the input text and get all the calibration values into an array
with open("./input.txt") as f:
    calibration_doc = f.read()

calibration_values = calibration_doc.split("\n")

"""Define mapping function to get the first and last digit in a string"""
def get_first_last_digit(text: str) -> int:
    #Get all
    digits = [x for x in text if not x.isalpha()]
    
    first_last_digit = digits[0] + digits[len(digits)-1]
    return int(first_last_digit)


calibration_sum = sum(map(get_first_last_digit, calibration_values))

print(calibration_sum)