# birth_year = input('Birth year: ')
# age = 2019 - birth_year
# print(age)
#
# #The above program produces below error
#
# Birth year: 1990
# Traceback (most recent call last):
#   File "C:/python/PythonPrograms/From_Mosh/type_conversion.py", line 2, in <module>
#     age = 2019 - birth_year
# TypeError: unsupported operand type(s) for -: 'int' and 'str'
# It will be treated like this by the interpreter
# 2019 - '2019'

# Whatever we type on terminal is treated as sting
# There are three functions used for converting
# int() = To convert string to integer
# float() = To convert string to float or a decimal number to float
# bool() = To convert string to boolean

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# type function is used to retrieve the what is the typeof the variable
# input function always retruns a string

# Exercise
# weight_pounds = input("Please enter your weight in pounds")
# kilo = int(weight_pounds) * 12.8
# print(kilo)
# print("Weight is KG is " + str(kilo))
# In the above line again typecasting required. as python cant concatinate string and flowat
