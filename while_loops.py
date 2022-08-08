"""
Program Author: Austin Mays
Program Name: input_while.py
Program Function: To allow the user a differing level of freedom in the numerical input of the values provided.
Date: 03/06/2022
"""

x=1
while x<100:
    x += int(input('Enter number to add:'))

print('The number entered is', x, ',which is more than 100', sep='')
"""
This gave the user no freedom to quit or have a self-stop compiled final list."""

input_list=[]
input_list_input = 100
while input_list_input != 'stop':
    input_list.append(input_list_input)
    input_list_input = input("Enter number until 101 is reached or type stop:")
print('Here is your completed list!')
print(input_list)
"""
This gave the user more freedom, and allowed for a compiled list even if no numbers were entered."""

for input_list in range(1,101,1):
    print(input_list)
"""
This final one was all automated, so the user could only see the number value skyrocket as they sat and watched, unable to interact in the slightest."""
