from account_basis import Account
from isa import Isa
from lisa import Lisa
import random


def main():
    new_dict = {}

    bank_script = input("Please select an operation from the following: \n1. Create account \n2. Modify account "
                        "\n3. Delete account \n4. Deposit \n5. Withdraw \n6. Check balance \n7. Quit \n")

    while bank_script != '7':
        # Create account
        if bank_script == '1':
            user_name = input("Please enter your name: ")
            user_pin = input("Please enter your 4-digit pin: ")
            account_id = random.randint(0, 1000)
            balance = 0
            print("Account created successfully, your account number is: " + str(account_id))
            user_account = Account(user_name, account_id, user_pin, balance)
            new_dict[account_id] = user_account
            print(new_dict)
            print(new_dict[account_id].get_balance())
            print(user_account.get_balance())

        # Modify account
        if bank_script == '2':
            acc_num_check = int(input("Please enter your account number: "))
            while acc_num_check not in new_dict:
                acc_num_check = int(input("Please enter your account number: "))

            if new_dict[acc_num_check].pin_check():
                print("Modify: Name, Pin")
                user_modify = input("Please enter your modification: ")

                if user_modify.lower() == 'name':
                    current_name = new_dict[acc_num_check].get_name()
                    print("Your current name is: " + current_name)
                    new_name = input("Please enter your updated name: ")

                    new_dict[acc_num_check].set_name(new_name)
                    print("Your updated name is: " + new_dict[acc_num_check].get_name())

                if user_modify.lower() == 'pin':
                    current_pin = new_dict[acc_num_check].get_pin()
                    print("Your current pin is: " + current_pin)
                    new_pin = int(input("Please enter your updated pin: "))

                    new_dict[acc_num_check].set_pin(new_pin)
                    print("Your updated pin is: " + str(new_dict[acc_num_check].get_pin()))
            else:
                print("The police are on their way :)")

        # Delete account
        if bank_script == '3':
            acc_num_check = int(input("Please enter your account number: "))
            while acc_num_check not in new_dict:
                acc_num_check = int(input("Please enter your account number: "))

            are_you_sure = input("Please type 'yes' to delete account " + str(acc_num_check)
                                 + " or q to return to menu: ")
            if are_you_sure.lower() == 'yes':
                del new_dict[acc_num_check]
                print("Account " + str() + " deleted")

        # Deposit
        if bank_script == '4':
            acc_num_check = int(input("Please enter your account number: "))
            while acc_num_check not in new_dict:
                acc_num_check = int(input("Please enter your account number: "))

            if new_dict[acc_num_check].pin_check():

                current_balance = new_dict[acc_num_check].get_balance()
                print("Your current balance is: £" + str(current_balance))

                user_deposit = int(input("Please enter the amount you would like to deposit (£): "))

                new_dict[acc_num_check].set_balance(current_balance + user_deposit)
                print("Your new balance is: £" + str(new_dict[acc_num_check].get_balance()))

            else:
                print("The police are on their way :)")
                break

        # Withdraw
        if bank_script == '5':
            acc_num_check = int(input("Please enter your account number: "))
            while acc_num_check not in new_dict:
                acc_num_check = int(input("Please enter your account number: "))

            if new_dict[acc_num_check].pin_check():

                current_balance = new_dict[acc_num_check].get_balance()
                print("Your current balance is: £" + str(current_balance))

                user_withdraw = int(input("Please enter the amount you would like to withdraw (£): "))

                new_dict[acc_num_check].set_balance(current_balance - user_withdraw)
                print("Your new balance is: £" + str(new_dict[acc_num_check].get_balance()))

            else:
                print("The police are on their way :)")
                break

        # Check balance
        if bank_script == '6':
            acc_num_check = int(input("Please enter your account number: "))
            while acc_num_check not in new_dict:
                acc_num_check = int(input("Please enter your account number: "))

            if new_dict[acc_num_check].pin_check():
                print("Your current balance is: £" + str(new_dict[acc_num_check].get_balance()))
            else:
                print("The police are on their way :)")

        bank_script = input("Please select an operation from the following: \n1. Create account \n2. Modify account "
                            "\n3. Delete account \n4. Deposit \n5. Withdraw \n6. Check balance \n7. Quit \n")


main()
