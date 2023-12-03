# Advent of Code 2023
# Day 1, Part 2
# December 2, 2023

import re

input_file = open("day1-input.dat", "r")

replacements = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
replacer = replacements.get

calib_total = 0

for line in input_file:

   calib_values     = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|zero))", line)
   calib_new_values = [replacer(n, n) for n in calib_values]
   calib_str        = calib_new_values[0] + calib_new_values[-1]
   calib_total     += int(calib_str)

   print("\n\nThe input line is                : ", line, end="")
   print("The regex extracted values are   : ", calib_values)
   print("The converted numeric values are : ", calib_new_values)
   print("first digit: ", calib_new_values[0], " / last digit: ", calib_new_values[-1], " / calib num = ", calib_str)

input_file.close()

print("\nThe sum of all calibration values is:", calib_total)
