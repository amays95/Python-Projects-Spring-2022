"""
Program Author: Austin Mays
Program Name: for_loops.py
Program Function: To print out the sequence of numerical values entered without further input from user.
Date: 03/06/2022
"""


num_list=[25.50, 30.55, 50.35, 88.20, 90.01]

add = 0
mult = 1
for x in num_list:
    add += x
    mult *= x

print(add, mult)

[99, 33]
for x in range(99, 31, -2):
    print(x)
else:
    print('Descent Complete')
