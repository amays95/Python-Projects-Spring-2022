"""
Program Author: Austin Mays
Program Name: hourly_employee_input_return.py
Program Function: To allow employees the ability to update their name, hours worked, and hourly rate of pay. This edition allows for a return to be sent back to user.
Date: 03/06/2022
"""
def hourly_employee_input():
    """This function prompts the user to input their name, total hours of work, and the pay rate per hour of said work."""


    try:
        name = str(input('Name:'))
        if name.isdigit():
            raise TypeError
    except TypeError:
            print('Your Name, not a Number please!')
    else:
        print('Saved')
    
    finally:
        print('Try Complete')

    try:                    
        hours_worked = int(input('Hours:'))
        if hours_worked<0:
            raise ValueError
    except ValueError:
        print('Negative Numbers Not Accepted')
        if input is str:
            raise ValueError
    except ValueError:
        print('Only Numbers Please')
    
    else:
        print('Saved')
    finally:
        print('Try Complete')


        

    try:
        hourly_pay_rate = float(input('Your Pay Rate:'))

        if hourly_pay_rate<0:
            raise ValueError
    except ValueError:
        print('Invalid: Negative Entered')
        
        if input is str and not float:
            raise ValueError
    except ValueError:
        print('Only Numbers Please')
        
    else:
        print('Saved')
    finally:
        print('Try Complete')

    if name.isalpha() and (hours_worked>=0) and (hourly_pay_rate>=0):
         print(name, hours_worked, hourly_pay_rate)
    else:
        print('Error Occurred: Inputs Not Valid!')

    try:
        weekly_pay = hours_worked*hourly_pay_rate
        if weekly_pay != hours_worked*hourly_pay_rate:
            print('Error Occurred')
        else:
            return name, weekly_pay
            print(name, weekly_pay)
    finally:
        print('Name/Weekly Pay:')

      


def weekly_pay(hours_worked, hourly_pay_rate):

    try:                    
        hours_worked = int(input('Hours:'))
        if hours_worked<0:
            raise ValueError
    except ValueError:
        print('Negative Numbers Not Accepted')
        if input is str:
            raise ValueError
    except ValueError:
        print('Only Numbers Please')
    
    else:
        print('Saved')
    finally:
        print('Try Complete')


        

    try:
        hourly_pay_rate = float(input('Your Pay Rate:'))

        if hourly_pay_rate<0:
            raise ValueError
    except ValueError:
        print('Invalid: Negative Entered')
        
        if input is str and not float:
            raise ValueError
    except ValueError:
        print('Only Numbers Please')
        
    else:
        print('Saved')
    finally:
        print('Try Complete')
total = weekly_pay

       
