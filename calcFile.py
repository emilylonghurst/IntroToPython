from calcFunctions import *


print("This program will calculate an operation of your choosing when given two numbers.")

user_list = [0]
history = []

while user_list[0] != "q":
    user_input = (input("Please enter your equation in the format num operator num (or type q to quit): "))

    if user_input[0] == "q" or user_input[0] == "Q":
        break
    elif user_input[0] == "h" or user_input[0] == "H":
        for x in history:
            print(x)

    user_list = check_length(user_input)

    if user_list == "q" or user_list == "Q":
        break

    first_number = user_list[0]
    first_number = check_number(first_number)

    operation_input = user_list[1]
    operation_input = check_operator(operation_input)

    second_number = user_list[2]
    second_number = check_number(second_number)

    history.append(user_input)

    calc(operation_input, first_number, second_number)