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
        return check_number(input("Please enter your first number: "))


def check_operator(operation):
    operation_list = ["add", "+", "subtract", "-", "multiply", "*", "divide", "/", "power", "**", "root"]
    if operation in operation_list:
        return operation
    else:
        return check_operator(input("Please type the operation you wish to perform from the list above: "))


print("This program will calculate an operation of your choosing when given two numbers.")

first_number = 0

while first_number != "q":
    first_number = check_number(input("Please enter your first number (or type q to quit): "))
    if first_number == "q" or first_number == "Q":
        break

    print("Please select an operator: Add, Subtract, Multiply, Divide, Power, Root")

    operation_input = check_operator(input("Please type the operation you wish to perform from the list above: "))

    second_number = check_number(input("Please enter your second number: "))

    calc()





