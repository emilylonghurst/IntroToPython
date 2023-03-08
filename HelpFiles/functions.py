# FUNCTIONS

# Every function should do just one thing

#######################################################

# # Declaring a function

# def print_hello():
#     print("Hello")
#
# # Calling a function - function invocation
#
#
# print_hello()

###########################################################

#
# def addition(num1, num2):
#     print(num1 + num2)
#
#
# # Can put in values or variables or numeracy
# addition(4, 8)
# addition(4-7, 1+9)
#
#
# var1 = 19
# var2 = -4
#
# addition(var1, var2)

#############################################################

# # Scope of variables
#
# def addition(num1, num2):
#     localVar = 9
#     print(num1 + num2)
#
# # Below will not work as num1 is defined inside the function
# # print(num1)
#
# # Below will not work as localVar is inside a function and is not defined in the body of the code
# # print(localVar)
#
# # Therefore, you can have duplicate variable names

###########################################################

# # Returning from function
# # Used if you want something back from the function
#
#
# def subtraction(num1, num2):
#     return num1 - num2
#
#
# # stores the result of the function into a variable called result
# result = subtraction(5, 9)
# print(result)

############################################################

# # Basic calculator using functions
#
# def getNumber():
#     num = input("Give me a number! ")
#     while not num.isdecimal():
#         print("That's not a number, try again")
#         num = input("Give me a number! ")
#     return int(num)
#
#
# def calculate(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#
#
# first = getNumber()
# second = getNumber()
#
#
# result = calculate(first, second, '+')
# print(result)

#############################################################

# # Highlight over a function, ctrl + click to see where the function is defined, try it on the print function
#
# print("Hi")

##############################################################

# # Modifying variables using functions
#
# def change(a):
#     a = 7
#
#
# myVar = 8
# change(myVar)
# # myVar will not be changed to 7, it will remain at 8 because 'a' is a local variable
# print(myVar)
#
# #########################
#
#
# # However, you can add things using a function. Doesn't need returning as it is adding to an initial list
# def change2(a):
#     a += ['hello', 'there']
#
#
# my_list = ['Martina']
# change2(my_list)
# print(my_list)

###############################################################

# # Function with a default parameter
# # Most tax in America is 20% (0.2) however some items have more
#
# # If you do not include the second parameter, the default value of 0.2 is used
# # If you DO include the second parameter, it will use what you specify
#
# def calculate_tax(price, tax=0.2):
#     result = price * (1 + tax)
#     return result
#
#
# book = 12
# chocolate = 5
# # Book and chocolate have the same tax
# print(calculate_tax(book, 0.2))
# print(calculate_tax(chocolate))
#
# gin = 20
# print(calculate_tax(gin, 0.3))
#
#
# # Default parameters HAVE to be on the right side otherwise it will not know whether you are specifying the value
# # If there are multiple default parameters you can specify which you want to alter by using tax = 0.3 for example
# # Otherwise you can rely on the position of the parameter
#
# #############
#
# # Enforce naming of parameters using a *
# # Anything after the star must be named
#
#
# def calculate_tax(*, price, tax=0.2):
#     result = price * (1 + tax)
#     return result
#
#
# print(calculate_tax(price=book))

##############################################################

