print('Thushalini Peranantham')
print('o----')
print(' ||||' * 3)

#variables in python are case sensitive and use normal rules to create
#can't use special characters

#basically can hold integer,floating point,string,character,and boolean

# #user input
# name = input('What is your name? ')
# color = input('Your favourite color? ')
# #in this name and color gets str input. If we want someother datatype then we have to do type conversion

# print('Hi ' + name)    #string concatenation
# print(name + ' likes ' + color)

#Type conversion
birth_year = int(input('Your birth year? '))
age = 2025 - birth_year
print('Age : ' , age)  #str + non str concatenation
print(type(age))