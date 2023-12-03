# Advent of Code 2023
# Day 2, Part 2
# December 3, 2023

import re

input_file = open("day2-input.dat", "r")

sum_power = 0

for line in input_file:
   max_r_cubes = 0
   max_g_cubes = 0
   max_b_cubes = 0
   line = line.rstrip()
   game_num   = int((line.split(': ')[0]).split(' ')[-1])
   game_cubes = (line.split(': ')[-1]).split('; ')
   #print(game_num, ': ', game_cubes)

   for draw in game_cubes:
      cubes = draw.split(', ')
      #print(cubes)

      for single_cube in cubes:
         #print(single_cube)
         cube_cnt = int(single_cube.split(' ')[0])
         cube_clr = single_cube.split(' ')[-1]
         #print('cube color: ', cube_clr)
         #print('cube count: ', cube_cnt)

         match cube_clr:
            case 'red':
               if cube_cnt > max_r_cubes:
                  max_r_cubes = cube_cnt
            case 'green':
               if cube_cnt > max_g_cubes:
                  max_g_cubes = cube_cnt
            case 'blue':
               if cube_cnt > max_b_cubes:
                  max_b_cubes = cube_cnt
            case _:
               print('color not found!')
   
   game_power = max_r_cubes * max_g_cubes * max_b_cubes
   sum_power += game_power

input_file.close()

print("\nThe sum of the power of the minimum cube sets is:", sum_power)
