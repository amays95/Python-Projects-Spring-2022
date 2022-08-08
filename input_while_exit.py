"""
Program Author: Austin Mays
Program Name: input_while_exit.py
Program Function: To allow the user a differing level of freedom in the numerical input of the values provided and to give user more freedom in the chose of an early exit from the program.
Date: 03/06/2022
"""

input_list=[]
input_list_input = 100
while input_list_input != 'stop':
    input_list.append(input_list_input)
    input_list_input = input("Enter number until 101 is reached or type 'stop' when finished or 'exit' to quit program:")
    if input_list_input == 'exit':
        print('So long friend!')
        break
print('Here is your completed list!')
print(input_list)
"""
This gave the user more freedom, and allowed for a compiled list even if no numbers were entered."""

for input_list in range(1,101,1):
    print(input_list)
"""
This final one was all automated, so the user could only see the number value skyrocket as they sat and watched, unable to interact in the slightest."""

"""Outcome was the same as input_while.py, except for the added option to exit the program all together."""
