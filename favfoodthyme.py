"""
Program Author: Austin Mays
Program Name: favfoodthyme.py
Program Function: This program gives the user the ability to input their favorite mealtime via check boxes and a rudimentary GUI.
Date: 3/27/2022

"""

import tkinter

"""

These four functions allow the GUI to portray four interactive options for the user to choose from.

"""

def breakfast():
    label.config(text='Yummy, a good breakfast is always important to a great day!')
def second():
    label.config(text='A second breakfast? You sure do love syrup, huh?!')
def lunch():
    label.config(text='Lunch is even better than brunch, if you prefer burgers to bagels of course.')
def dinner():
    label.config(text='A splendid end to a long day of work is a well cooked meal.')

m = tkinter.Tk()
m.title('Favorite Meal')
var_01 = tkinter.IntVar()
check_01 = tkinter.Checkbutton(m, text = 'Breakfast', variable = var_01, command=breakfast).grid(row=1)
var_02 = tkinter.IntVar()
check_02 = tkinter.Checkbutton(m, text = 'Second Breakfast', variable = var_02, command=second).grid(row=2)
var_03 = tkinter.IntVar()
check_03 = tkinter.Checkbutton(m, text = 'Lunch', variable = var_03, command=lunch).grid(row=3)
var_04 = tkinter.IntVar()
check_04 = tkinter.Checkbutton(m, text = 'Dinner', variable = var_04, command=dinner).grid(row=4)
label = tkinter.Label(m, text='Waiting')
label.grid(row=5)
exiting = tkinter.Button(m, text = 'Exit', width = 25, command = m.destroy)
exiting.grid(row=6)
