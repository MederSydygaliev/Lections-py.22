# Операторы сравнения -  <, >, == (equal) , >=, <=, != (not equal)

# логические операторы -


# num1 = 18
# num = 15
# print (18 < 15)
# print(type(5))

# Stroka = 'Hello'
# Stroka = 'World'
# print(ord('H'))
# print(ord('W'))
# ------------------ASCII code


# ----------------------------------------------

# text = 'Hello mthrfkrs'
# for letter in text:
#     print(ord(letter))

# print (chr(1012)) 


# -----------------------------------------

# условные операторы - if, elif, else

# if <condition> :
#     <body if>
#     <body if> сработает если в if придет true
    
# if <condition> :
#     <body if>
#     <body if> сработает если в if придет true

#  elif <condition> :
#       <body elif>
#  elif <condition> :
#       <body elif>\
#  elif <condition> :
#       <body elif>
# else:
#     <body>

# string = input('enter smthng: ')
# if string == 'Hello':
#    print('Hello stranger')
# elif string == 'John':
#    print('Hi john')
# elif string == 'Mercedes':
#    print('benz is great')
# else:
#     print('what is going on')
# print ('bye bye')

# ---------------------------------------

# email = input('enter your mail adress: ')
# password1 = input ('enter new password: ')
# password2 = input('confirm password: ')
# if len(password1) < 8:
#     raise Exception('enter minimum 8 symbols!')
# elif password1 != password2:
#     raise Exception('Password did\'t match')
# else:
#     print('Successfuly signed up!')

# ---------------------------------------------------
# from curses.ascii import isdigit


# age = input('Enter your age: ')
# if age.isdigit():
#     age = int(age)
# else: 
#     raise ValueError('Enter numbers!')
# if age < 18:
#     print(f'You can come back after {18 - age} years!')
# else:
#     print('You\'r welcome mthrfckr!!!')
# ------------------------------------------------------------------



from curses.ascii import isalnum, isalpha, isdigit
from string import digits
from unicodedata import digit

password = input('Enter your password: ')
symbols = ['_', '.', '%', '#', '@', ',', '-', '+','*']
flag = False
for element in symbols:
    if element in password:
        flag = True
x = digit()
digi = False
for element1 in x:
    if element1 in password:
        digi = True
if password.isalpha():
    raise Exception('password must include digits!')
elif not digi:
    print('password must include letters')
elif not flag:
    raise Exception('vy ne vveli hotya by 1 spec symbol')
else:
    print('OKOKOK')

    


