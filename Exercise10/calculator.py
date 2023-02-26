

print("This program will calculate an operation of your choosing when given two numbers.")

# while loop keeps the program running unless the user enters q when prompted for first_number
# make it separate loop(s), only put things that need repeating into the loops

# ask for first_number first, then do while if first_number is not q
while True:
    first_number = input("Please enter your first number (or type q to quit): ")

    if first_number == "q":
        break

    # Checks if first_number is a number (.isdigit() does not work for floats)

    try:
        first_number = float(first_number)

    except ValueError:
        first_number = float(input("Please enter your first number: "))

# asks user for an operation

    print("Please select an operator: Add, Subtract, Multiply, Divide, Power, Root")

    operation_input = input("Please type the operation you wish to perform from the list above: ")

    operation_list = ["add", "+", "subtract", "-", "multiply", "*", "divide", "/", "root"]

# while loop checks if the operation is within operation_list (permitted operations)
    while True:
        if operation_input.lower() in operation_list:

            # asks user for another number and checks that it is a float

            second_number = input("Please enter your second number: ")

            try:
                second_number = float(second_number)

            except ValueError:
                second_number = float(input("Please enter your second number: "))

            # if statements perform the selected operation regardless of string, symbol or capitalisation

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

            break

        else:
            operation_input = input("Please type the operation you wish to perform from the list above: ")
