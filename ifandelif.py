Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

welcome = input('Sign up here:')
Sign up here:
name = input('First Name' 'Last Name')
First NameLast Name
name = input('First Name' ' ' 'Last Name')
First Name Last Name
membership = input('Select Membership Tier:')
Select Membership Tier:

tier_01 = ('Platinum' + 60)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tier_01 = ('Platinum' + 60)
TypeError: can only concatenate str (not "int") to str
tiers = ['Platinum: $60.00', 'Gold: $50.00', 'Silver: $40.00', 'Bronze: $30.00', 'Free Trial: Free']
tiers
['Platinum: $60.00', 'Gold: $50.00', 'Silver: $40.00', 'Bronze: $30.00', 'Free Trial: Free']
platinum = 60
gold = 50
silver = 40
bronze = 30
freetrial = 0

if platinum > gold:
    print('$60.00')
elif platinum >= gold:
    print('$50.00')
else:
    print('The beaver builds his dam quickly')

    
$60.00

if gold > platinum:
    print('$50.00')
elif silver < gold:
    print('$50.00')
else:
    print('daring duo dashes dutifully')

    
$50.00
if bronze == silver:
    print('$30.00')
elif bronze!=silver:
    print('$40.00')
else:
    print('seashells by the seashore')

    
$40.00
if bronze != bronze:
    print('Free Trial')
elif bronze == bronze:
    print('$30.00')
else:
    print('terror in the system')

    
$30.00
if bronze > freetrial:
    print('Free Trial')
elif freetrial > platinum:
    print('$100.00')
else:
    print('Welcome to the end of the assignment')

    
Free Trial
"""
Student's Name: Austin Mays
Program Name: ifandelif.py
Date: 02/27/2022
"""
"\nStudent's Name: Austin Mays\nProgram Name: ifandelif.py\nDate: 02/27/2022\n"
