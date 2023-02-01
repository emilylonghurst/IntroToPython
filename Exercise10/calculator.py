import math

print("This program will calculate an operation of your choosing when given two numbers.")

first_number = input("Please enter your first number: ")

# Checks if first_number is a number (.isdigit() does not work for floats)
try:
    first_number = float(first_number)
    
except ValueError:
    first_number = input("Please enter your first number: ")

second_number = input("Please enter your second number: ")

try:
    second_number = float(second_number)

except ValueError:
    second_number = input("Please enter your second number: ")

print("Possible operations: Add, Subtract, Multiply, Divide, Power, Root")

operation_input = input("Please type the operation you wish to perform from the list above: ")

try:
    if operation_input.lower() == "add":
        print(first_number + second_number)
    elif operation_input.lower() == "subtract":
        print(first_number - second_number)
    elif operation_input.lower() == "multiply":
        print(first_number * second_number)
    elif operation_input.lower() == "divide":
        print(first_number / second_number)
    elif operation_input.lower() == "power":
        print(first_number ** second_number)
    elif operation_input.lower() == "root":
        print(first_number ** (1 / second_number))
except ValueError:
    operation_input = input("Please type the operation you wish to perform from the list above: ")
