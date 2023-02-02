
import getpass

# pin = 1414
# supplied_pin = input("Enter your PIN: ")
#
# i = 0
# while i < 2:
#     if supplied_pin == str(pin):
#         print("Correct PIN entered")
#         i = 2
#     else:
#         print("PIN incorrect, you have " + str(2 - i) + " tries remaining")
#         supplied_pin = input("Enter your PIN: ")
#         i += 1
#         if i == 2:
#             print("Too many incorrect PINs entered")

# Make sure the run configuration is set to pinProgram.py
# Enable 'emulate terminal in output console' in Configurations - pinProgram - edit

pin = 1414
supplied_pin = getpass.getpass(prompt="Enter your PIN: ")

i = 0
while i < 2:
    if supplied_pin == str(pin):
        print("Correct PIN entered")
        i = 2
    else:
        print("PIN incorrect, you have " + str(2 - i) + " tries remaining")
        supplied_pin = getpass.getpass(prompt="Enter your PIN: ")
        i += 1
        if i == 2:
            print("Too many incorrect PINs entered")
