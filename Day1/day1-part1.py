# Advent of Code 2023
# Day 1, Part 1
# December 2, 2023

import re

input_file = open("day1-input.dat", "r")

calib_total = 0

for line in input_file:

   calib_values = re.findall("[0-9]", line)
   calib_str = calib_values[0] + calib_values[-1]
   calib_total += int(calib_str)

   print("\n\nThe input line is                : ", line, end="")
   print("The regex extracted values are   : ", calib_values)
   print("first digit: ", calib_values[0], " / last digit: ", calib_values[-1], " / calib num = ", calib_str)

input_file.close()

print("\nThe sum of all calibration values is:", calib_total)
