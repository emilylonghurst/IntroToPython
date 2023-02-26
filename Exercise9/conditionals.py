
# my_num = int(input("Give me a number: "))
# if my_num > 5:
#     print("You gave me a number greater than five")
# else:
#     print("You gave me a number less than five")

########################################################

# my_num = 0
# my_input = input("Give me a number: ")
# if my_input.isdecimal():
#     my_num = int(my_input)
#     if my_num > 5:
#         print("You gave me a number greater than five")
#     else:
#         print("You gave me a number less than five")
# else:
#     print("That's not a number")

#########################################################

# # change colour to red, amber, green or other
# light = input("Choose a traffic light colour: ")
#
# # check for equality
# if light == 'red':
#     print("Stop!!")
# # elif = else if
# elif light == 'amber':
#     print("Watch out!")
# elif light == 'green':
#     print("Go!")
# else:
#     print("Lights are broken!")

#########################################################

# user_input = input("Type something: ")
# # ! = logical NOT
# if user_input != '':
#     print(user_input.upper())
# else:
#     print("You have not typed anything")


# This does the same thing as above, an empty string evaluates to false automatically, no need to add != '':
# user_input = input("Type something: ")
# if user_input:
#     print(user_input.upper())
# else:
#     print("You have not typed anything")

###########################################################

# my_list = ['chocolate', 'tea', 'scones']
# # The .lower converts the input into lower case to make it match the list, so it is not case-sensitive
# if 'chocolate'.lower() in my_list:
#     print("We are good")
# else:
#     print("Add chocolate immediately")

##########################################################

# # or
# bus = 67
# if bus == 67 or bus == 100:
#     print("I am getting on")
# else:
#     print("I am not getting on")

##########################################################

# LOOPS

# While loops

# i = 0
# while i < 7:
#     print(i)
#     i += 1


# Ask the user for a number, will keep asking until a number is given

# my_input = input("Type a number: ")
# while not my_input.isdecimal():
#     my_input = input("Type a number: ")

############################################################

# For loops

# my_list = ['chocolate', 'tea', 'scones']
# # for every element in my_list do ...
# # can use any variable name for 'element' i.e. for e in my_list print(e) will also work
# for element in my_list:
#     print(element)

# How to use a for loop like a while loop

# i = 0
# while i < 5:
#     print("hello")
#     i += 1
#
# # for i in [1, 2, 3, 4, 5] - last number in range is not included
# for i in range(1, 6):
#     print("hello")

########################################################

# Checks if even number as even numbers divided by 2 == 0

# for i in range(1, 6):
#     if i % 2 ==0:
#         print(i)
#     else:
#         continue
#     print("hello")
#
#########################################################

# my_list = ['chocolate', 'tea', 'scones']
# for e in my_list:
#     print(e)
#
#
# my_list = ['chocolate', 'tea', 'scones']
# for pos, e in enumerate(my_list):
#     print(e + " is on position " + str(pos))

########################################################

# range(start,stop, stepSize*) => start, start+stepSize, start+stepSize, start+stepSize, ... stop-1

# for i in range(0,5,2):
#     print(i)

##########################################################

# # your loop can have an else part
#
# for i in range(0,3):
#     print(i)
# else:
#     # this will not run if the loop stops unnaturally i.e. from a break
#     # only run when the loop is exhausted, it stops naturally
#     print("I'm done")

############################################################
#
# num = input("type in a number")
# while not num.isdecimal():
#     print("That's not a number!!")
#     num = input("type in a decimal")
# else:
#     num_int = int(num)
#
# ###########################################################
#
# a = int(input("Type in first number"))
# b = int(input("Type in second number"))
# max_num = 0
#
# if a > b:
#     max_num = a
# else:
#     max_num = b
#
# print(max_num)
#
#
# # The above can be condensed into one expression:
#
# max_num = a if a > b else b
#
# print(max_num)
#
# # has to have the else part to work
#
# ##########################################################
