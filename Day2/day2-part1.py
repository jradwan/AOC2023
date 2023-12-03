# Advent of Code 2023
# Day 2, Part 1
# December 3, 2023

import re

input_file = open("day2-input.dat", "r")

r_cubes  = 12
g_cubes  = 13
b_cubes  = 14
id_total = 0

for line in input_file:
   possible = True
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
               if cube_cnt > r_cubes:
                  possible = False
                  #print('impossible game found - ', str(cube_cnt), ' red')
            case 'green':
               if cube_cnt > g_cubes:
                  possible = False
                  #print('impossible game found - ', str(cube_cnt), ' green')
            case 'blue':
               if cube_cnt > b_cubes:
                  possible = False
                  #print('impossible game found - ', str(cube_cnt), ' blue')
            case _:
               print('color not found!')
   
   if possible:
      id_total += game_num

input_file.close()

print("\nThe sum of the IDs of all possible games is:", id_total)
