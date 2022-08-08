"""
Program Author: Austin Mays
Program Name: average_score.py
Program Function: To output the given values of test scores into a mean final result.
Date: 02/27/2022
"""
'\nProgram Author: Austin Mays\nProgram Name: average_score.py\nProgram Function: To output the given values of test scores into a mean final result.\nDate: 02/27/2022\n'

score_cap = 100


def user_information(last_name, first_name, age):
    """Prompts users for last name, first name, and age."""

try:
    last_name = str(input('Last Name:'))

    if int is not str:
        raise TypeError('No numbers allowed')
    
except TypeError:
    """This brings up error in code."""

    print('No numbers allowed')
else:
    print(last_name)
    
finally:
    print('Try Complete')
try: 
    first_name = str(input('First Name:'))
    
    if int is not str:
        raise TypeError('No numbers allowed')
except TypeError:
    print('No numbers allowed')
else:
    print(first_name)
finally:
    print('Try Complete')

try:
    age = int(input('Enter your age:'))

    if age<0:
        raise ValueError('Invalid age')
except ValueError:
    print('Invalid age')
else:
    print(age)
finally:
    print('Try Complete')

def test_information(score_01, score_02, score_03):
    """This function prompts the user to input the following testing information."""

try:
    score_01 = int(input('Score 1:'))
    if score_01 < 0:
        raise ValueError('Negative Score Entered')
except ValueError:
    print('Negative Score Entered')
else:
    print(score_01)
finally:
    print('Next Score')

try:
    score_02 = int(input('Score 2:'))
    if score_02 < 0:
        raise ValueError('Negative Score Entered')
except ValueError:
    print('Negative Score Entered')
else:
    print(score_02)
finally:
    print('Next Score')

try:
    score_03 = int(input('Score 3:'))
    if score_03 < 0:
        raise ValueError('Negative Score Entered')
except ValueError:
    print('Negative Score Entered')
else:
    print(score_03)
finally:
    print('Total Average Score Below')

def average_score_calculation(scores, add, num_terms, mean, avg_score):
    """This function prompts the user to calculate their average score from the information provided above."""

try:
    scores = (score_01, score_02, score_03)
    if not int:
        raise ValueError
except ValueError:
    print('Value Not Recognized')
else:
    print(scores)
finally:
    print('Try Complete')

try:
    add = sum(scores)
    print(add)

    if add == len(scores):
        raise TypeError
except TypeError:
    print('type incorrect - add score totals not number of scores')
else:
    print(add)
finally:
    print('Addition Complete')

try:
    num_terms = len(scores)
    print(num_terms)

    if num_terms != len(scores):
        raise TypeError
except TypeError:
    print('type incorrect - add total number of tests, not the scores themselves')

else:
    print('Addition Complete')

finally:
    print('Now you must divide the total of the scores with the total of the tests')

try:
    mean = add/num_terms

    if mean != add/num_terms:
        raise ValueError
except ValueError:
    print('Value Not Recognized')
    
else:
    print('Mean Solved')

finally:
    print('Try Complete')
    
try:
    avg_score = (mean)
    if avg_score < 0:
        raise ValueError('Negative Average Not Allowed')
except ValueError:
    print('Negative Average Not Allowed')
else:
    print('No Error Found')
finally:
    print(avg_score)

print('Try Exercise Complete')
    

"""
test_1:84
test_2:95
test_3:71
scores = [84, 95, 71]
add = sum(scores)
num_terms = len(scores)
mean = add/num_terms
print(mean)
83.33333333333333
avg_score = 83.33'
lastname = 'Trill'
firstname = 'Alex'
f'Last Name:{lastname} First Name:{firstname} Age:{age+22} Average Score:{avg_score}'
f'Last Name:{lastname} First Name:{firstname} Age:{age+22} Average Score:{avg_score}'
'Last Name:Trill First Name:Alex Age:22 Average Score:83.33'
"""

                          
"""
I found it most helpful to have the import function as it kept the static constant while allowing for dynamic variables to flow seemlessly when running my code through.
"""
