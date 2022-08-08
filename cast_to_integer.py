"""
Program:cast_to_integer.py
Author: Austin Mays
Last date modified: 02/20/2022

The purpose of this program is to accept any input, convert to a integer type and output the integer.
"""

x=int(15)
print(x)

y=float('50')
print(y)

z=str(15+50)
print(z)

alpha=str(15)+str(50)
print(alpha)

"""
#Input,             Expected Output, Actual Output
#15                 15                 15
#50                 50.0               50.0
#str(15+50)         ?                  65
#str(15)+str(50)    ?                  1550
"""

"""
Inserting the string after inputting the integer and float parameters showed how the float and integer combined in two separate ways within the string. First, when combined together inside
parenthesis they act as a normal addition problem, equaling in this case 65. When put separate with two str values, one representing each, they combine into each other, making 1550. No addition, but two
numbers made one.
"""
