def calc():
    if operation_input.lower() == "add" or operation_input.lower() == "+":
        print(first_number + second_number)
    elif operation_input.lower() == "subtract" or operation_input.lower() == "-":
        print(first_number - second_number)
    elif operation_input.lower() == "multiply" or operation_input.lower() == "*":
        print(first_number * second_number)
    elif operation_input.lower() == "divide" or operation_input.lower() == "/":
        print(first_number / second_number)
    elif operation_input.lower() == "power" or operation_input.lower() == "**":
        print(first_number ** second_number)
    elif operation_input.lower() == "root":
        print(first_number ** (1 / second_number))


def check_number(num):
    try:
        num = float(num)
        return num
    except ValueError:
        return check_number(input("Please try again. enter another number: "))


def check_operator(operation):
    operation_list = ["add", "+", "subtract", "-", "multiply", "*", "divide", "/", "power", "**", "root"]
    if operation in operation_list:
        return operation
    else:
        return check_operator(input("Please type the operation you wish to perform from the list above: "))


# def check_length(userList):
#     print(len(userList))
#     if len(userList) != 3:
#       return check_length(input("Please enter your equation in the format num operator num (or type q to quit): ").split())
#     else:
#         return userList

def check_length(userList):
    if userList == " ":
        return check_length(input("Please enter your equation in the format num operator num (or type q to quit): "))
    else:
        user_split = userList.split()

    if len(user_split) != 3:
        return check_length(input("Please enter your equation in the format num operator num (or type q to quit): "))
    else:
        return user_split


print("This program will calculate an operation of your choosing when given two numbers.")

user_list = [0]

while user_list[0] != "q":
    user_input = (input("Please enter your equation in the format num operator num (or type q to quit): "))

    if user_input[0] == "q" or user_input[0] == "Q":
        break

    # if len(user_list) < 3:
    #    repeat again pls
    user_list = check_length(user_input)

    first_number = user_list[0]
    first_number = check_number(first_number)

    operation_input = user_list[1]
    operation_input = check_operator(operation_input)

    second_number = user_list[2]
    second_number = check_number(second_number)

    calc()
