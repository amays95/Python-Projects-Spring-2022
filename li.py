"""
Program Author: Austin Mays
Program Name: basic_list.py
Program Function: To take in user input data and return the variables as a list.
Date: 3/13/2022
"""
num = (0, 1, 2)
def get_input(month, day, birth):
    m = month
    d = day
    b = birth
    month = str(input('Enter your birth month:'))
    day = str(input('Enter your birthday'))
    birth = str(input('Enter your birth year:'))
    user_values = [month, day, birth]
    return user_values


def make_list(num):
    n = num
    num = (0, 1, 2)
    user_input = + 1
    while user_input <= 2:
        return user_input
    if user_input is not int:
        return ValueError
    else:
        return user_input
