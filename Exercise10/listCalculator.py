
print("This program will calculate an operation of your choosing when given two numbers.")

user_input = input("Please provide two numbers and an operator seperated by commas")

user_list = user_input.split(',')
print(type(user_list))
print(list(map(int, user_list)))

# equation = ("{0} + {1}".format(e, yournum))