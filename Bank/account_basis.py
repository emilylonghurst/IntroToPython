import random


class Account:

    def __init__(self, acc_name, acc_number, acc_pin, acc_balance=0):
        self._name = acc_name
        self._number = acc_number
        self._pin = acc_pin
        self._balance = acc_balance

    # balance getter method
    def get_balance(self):
        return self._balance

    # balance setter method
    def set_balance(self, new_balance):
        self._balance = new_balance

    def get_pin(self):
        return self._pin

    def set_pin(self, new_pin):
        self._pin = new_pin

    def pin_check(self):
        i = 0
        while i < 3:
            pin_test = int(input("Please enter your 4-digit pin: "))
            if pin_test == int(self._pin):
                return True
            else:
                i += 1
                print("You have " + str(3 - i) + " tries remaining")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
