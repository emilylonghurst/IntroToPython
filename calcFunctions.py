def calc(operation_input, first_number, second_number):
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


def check_length(userList):

    if userList == "q" or userList == "Q":
        return userList

    if userList == " ":
        return check_length(input("Please enter your equation in the format num operator num (or type q to quit): "))
    else:
        user_split = userList.split()

    if len(user_split) != 3:
        return check_length(input("Please enter your equation in the format num operator num (or type q to quit): "))
    else:
        return user_split

