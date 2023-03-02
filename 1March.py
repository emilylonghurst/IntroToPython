## FUNCTIONS
#
# # Use verbs at the beginning of functions to make variable naming easier
# def get_user_input():
#     user_in = input("Give me a number!")
#     return user_in
#
# user_input = get_user_input()

##############################################################################
#
# # STARS IN FUNCTION CALLING
#
# # Unpacking
#
# my_tuple = (4, 5, 6)
# num1, num2, num3 = my_tuple
#
#
# def do_sum(a, b, c):
#     return a + b + c
#
#
# print(do_sum(2, 3, 4))
# print(do_sum(num1, num2, num3))
#
# # calling the function, unpacking the elements in my_tuple into the parameters of the function by using the star
# print(do_sum(*my_tuple))
#
# ############################################
#
# # Two stars in function calling - unpacks a dictionary
# # FIX THIS
# def print_vat(**kwargs):
#     print(kwargs)
#
#
# vat = dict(vatpc=15, gross=9.55, message='Summary')
#
# print_vat(vat)

################################################################################

# # STARS WITHIN FUNCTION DECLARATION
#
# # Packing
# # stars can also be used in the declaration of a function
#
# # Variadic function - variable number of parameters
# # One parameter called name and then any other parameters will be assigned to stuff in a tuple
# def do_printing(name, *stuff):
#     print("Hello " + name)
#     print(stuff)
#
#
# do_printing("Name", "Everything", "Else", "Packed", "Into", "Stuff")
#
#
# ################################
# # Two stars in function declaration - Means it will be packed into a dictionary
#
# def print_vat(**kwargs):
#     print(kwargs)
#
#
# print_vat(vatpc=15, gross=9.55, message='Summary')

#############################################################################

# # Function returns a tuple of two values
#
# def keep_count(user, comp, status):
#     if status == 'user':
#         user += 1
#     else:
#         comp += 1
#     return user, comp
#
# # return user, comp looks like it is returning two variables, but it is just a tuple (user, comp) simplified
# # without the brackets ()
#
# running_total_u = 1
# running_total_c = 1
#
# # A tuple is returned from the function
# result_tuple = keep_count(running_total_u, running_total_c, 'user')
# print(result_tuple)
#
# # unpacking the tuple
# running_total_u, running_total_c = result_tuple
# print(running_total_u)
# print(running_total_c)
#
# # unpacking in one line
# running_total_u, running_total_c = keep_count(running_total_u, running_total_c, 'user')

############################################################################

# # Use with Caution!
#
# # The below function won't change a to 7 as this a is on the other planet
# def my_func(a):
#     a = 7
#
#
# # This function will change a as it uses the global a - Not a pure function so not the best way to do it
# def my_func2(b):
#     global a
#     a = 5
#
#
# a = 6
# my_func2(a)
# print(a)

#########################################################################

# # FUNCTIONS WITHIN FUNCTIONS
# # Functional programming
#
# def my_func(a):
#     print(a)
#
#
# def my_func3(f):
#     # invoking the function
#     # this will be my_func(2) so my_func will then print it out
#     f(2)
#
#
# # Passing a function into a function
# my_func3(my_func)


##########################################################################

# # Another example
#
# def my_func(a):
#     print(a)
#
#
# def my_func3(f):
#     # invoking the function
#     # this will be my_func(2) so my_func will then print it out
#     f(2)
#
#
# def triple(a):
#     print(a * 3)
#
#
# def double(a):
#     print(a * 2)
#
#
# # Passing a function into a function
# my_func3(my_func)
# my_func3(triple)
# my_func3(double)

#######################################################################

# # Another example
#
# def my_func(a):
#     print(a)
#
#
# def my_func3(f, num):
#     # invoking the function
#     # this will be my_func(2) so my_func will then print it out
#     f(2)
#
#
# def triple(a):
#     print(a * 3)
#
#
# def double(a):
#     print(a * 2)
#
#
# # Passing a function into a function
# my_func3(my_func, 7)
# my_func3(triple, 3)
# my_func3(double, 8)

##########################################################################

# # LAMBDA Functions
# # Have no name so cannot be called like a regular function
# # Used when you want an action, not a value
# # Typically used on one line of code, otherwise a regular function is used
#
# lambda a: print(a)
#
# my_func3(lambda a: print(a), 8)
#
# my_anon_func = lambda a: print(a * 4)
# my_anon_func(43)
#
# # Function equivalent:
# # my_anon_func(a)
# #   print(a*4)
#
#
# # my_anon_func = print(a*4)
# # The above would not work as the variable cannot store a print function
# # also, my_anon_func() allows you to use an action on a variable

###########################################################################

# Using a function from a different file
# Will run the file's code

# import pythonFile

# var = pythonFile.functionName()

# Or specify the function

# from pythonFile import functionName

# var = pythonFile.functionName()

#########################################################################

# The 'main' trick
# This code is put in the file you are importing to stop it running all the code

# if __name__ = "__main__":
#     num1 = get_number()
#     print(num1)

# If I am running the code, the file name will be Main, if imported it will be a different name,
# so it will only import the functions


##########################################################################

# # DOCSTRINGS
# # """ """ Creates a docstring in a function to explain it
# # Hover over the function if it has a docstring, and it will have your explanation at the bottom
#
# def getNum(num):
#     """Gets a number"""
#     print(num)

#########################################################################
