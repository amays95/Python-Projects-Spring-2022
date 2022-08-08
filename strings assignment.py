Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
movie character = 'Darth Vader'
SyntaxError: invalid syntax
movie_character = 'Darth Vader'
movie = 'Star Wars'
print(movie_character, movie)
Darth Vader Star Wars
print(len(movie_character))
11
capitalize(movie_character, movie)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    capitalize(movie_character, movie)
NameError: name 'capitalize' is not defined
capitalize
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    capitalize
NameError: name 'capitalize' is not defined
str.capitalize(movie_character, movie)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str.capitalize(movie_character, movie)
TypeError: str.capitalize() takes no arguments (1 given)
str.capitalize()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    str.capitalize()
TypeError: unbound method str.capitalize() needs an argument
movie_character = str('Darth Vader')
movie = str('Star Wars')
str.capitalize(movie_character, movie)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    str.capitalize(movie_character, movie)
TypeError: str.capitalize() takes no arguments (1 given)
str.capitalize(movie_character+movie)
'Darth vaderstar wars'
str.capitalize(movie_character)
'Darth vader'
favorite = 'Darth Vader in Star Wars'
favorite = str('Darth Vader in Star Wars')
str.capitalize(favorite)
'Darth vader in star wars'
favorite_1 = 'Darth'
favorite_2 = 'Vader'
favorite_3 = 'Star'
favorite_4 = 'Wars'
favorite_1 = str('Darth')
favorite_1 = 'Darth'
favorite_2 = 'Vader in'
favorite_3 = 'Star'
favorite_4 = 'Wars'
capitalize(favorite_1, favorite_2, favorite_3, favorite_4)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    capitalize(favorite_1, favorite_2, favorite_3, favorite_4)
NameError: name 'capitalize' is not defined
capitalize('Darth','Vader in','Star', 'Wars')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    capitalize('Darth','Vader in','Star', 'Wars')
NameError: name 'capitalize' is not defined
str='Darth Vader in Star Wars'
capitalized_str = str.capitalize()
print('Darth Vader in Star Wars', capitalized_string)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print('Darth Vader in Star Wars', capitalized_string)
NameError: name 'capitalized_string' is not defined. Did you mean: 'capitalized_str'?
print('Darth Vader in Star Wars', capitalized_str)
Darth Vader in Star Wars Darth vader in star wars
print(capitalized_str)
Darth vader in star wars
print(str.find('Vader'))
6
result = str.index('in')
print(result)
12
result = str.isalnum()
print(result)
False
result = str.isalpha()
print(result)
False
result = str.isdigit()
print(result)
False
result = str.islower()
print(result)
False
result = str.isupper()
print(result)
False
result = str.isspace()
print(result)
False
result = str.startswith('Darth')
print(result)
True

================================ RESTART: Shell ================================
list_one = ['blue','sky','clouds']
print(list_one)
['blue', 'sky', 'clouds']
list_one.append('white')
print(list_one)
['blue', 'sky', 'clouds', 'white']
list_two = ['red','rocks','yellow']
result = list_one.copy(list_two)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    result = list_one.copy(list_two)
TypeError: list.copy() takes no arguments (1 given)
result = list_one.copy()
print(result)
['blue', 'sky', 'clouds', 'white']
x = list_one.copy()
y = list_two.copy()
print(x,y)
['blue', 'sky', 'clouds', 'white'] ['red', 'rocks', 'yellow']
print(x+y)
['blue', 'sky', 'clouds', 'white', 'red', 'rocks', 'yellow']
x = list_one.index('blue')
y = list_one.index('tapestry')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    y = list_one.index('tapestry')
ValueError: 'tapestry' is not in list
x = list_one.count('white')
print(x)
1
list_one.insert(5, 'sky')
print(list_one)
['blue', 'sky', 'clouds', 'white', 'sky']
list_one.remove('blue')
print(list_one)
['sky', 'clouds', 'white', 'sky']
list_one.reverse()
print(list_one)
['sky', 'white', 'clouds', 'sky']
list_one.sort()
print(list_one)
['clouds', 'sky', 'sky', 'white']
list_one.clear()
print(list_one)
[]
