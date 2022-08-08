Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
MAX = 10
MIN = 0
y=5
y>MAX
False
y<MIN
False
x=15
if MIN<x<MAX:
    print("x is between 0 and 10.")

    
if MIN<x<MAX:
    print("x is between 0 and 10.")
else:
    print("x is not between 0 and 10.")

    
x is not between 0 and 10.

if MIN<=X!=MAX:
    print("x is greater than or equal to 0, but not equal to 10.")
else:
    print("x is not greater than or equal to 0.")

    
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    if MIN<=X!=MAX:
NameError: name 'X' is not defined. Did you mean: 'x'?
if MIN<=x!=MAX:
    print("x is greater than or equal to 0, but not equal to 10.")
else:
    print("x is not greater than or equal to 0.")

    
x is greater than or equal to 0, but not equal to 10.
if MAX!=x>=MIN:
    print("x is greater than or equal to 0, but not equal to 10.")
else:
    print("x is not greater than or equal to 0.")

    
x is greater than or equal to 0, but not equal to 10.
if MAX<>x>=MIN:
    
SyntaxError: invalid syntax
if MIN<=x!=MAX:
    print("x is greater than or equal to 0, but not equal to 10.")
else:
    print("x is greater than 0 and 10.")

    
x is greater than or equal to 0, but not equal to 10.
if MIN==x<MAX:
    print("x is greater than or equal to 0, but not equal to 10.")
else:
    print("x is greater than both 0 and 10.")

    
x is greater than both 0 and 10.

if MIN<x<=MAX:
    print("x is greater than 0 and less than or equal to 10.")
else:
    print("x is greater than 0 and 10.")

    
x is greater than 0 and 10.
