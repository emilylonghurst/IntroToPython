
import random

# COMMENTED FUNCTIONS HAVE COMBINED INTO ONE

# def computerConvert(number):
#     if computerChoice == 0:
#         number = 'R'
#     elif computerChoice == 1:
#         number = 'P'
#     elif computerChoice == 2:
#         number = 'S'
#     return number
#
#
# def humanConvert(rps):
#     final = 0
#     if rps.upper() == 'R':
#         final = 'Rock'
#     elif rps.upper() == 'P':
#         final = 'Paper'
#     elif rps.upper() == 'S':
#         final = 'Scissors'
#     return final


def convert(rps):
    result = 0
    if rps == 'r' or rps == 'R' or rps == 0:
        result = 'Rock'
    if rps == 'p' or rps == 'P' or rps == 1:
        result = 'Paper'
    if rps == 's' or rps == 'S' or rps == 2:
        result = 'Scissors'
    return result


def whoWins(human, computer):
    if human == computer:
        print("It's a draw!")
    elif human == "Rock" and computer == "Paper":
        print("Computer wins!")
    elif human == "Rock" and computer == "Scissors":
        print("You win!")
    elif human == "Paper" and computer == "Rock":
        print("You win!")
    elif human == "Paper" and computer == "Scissors":
        print("Computer wins!")
    elif human == "Scissors" and computer == "Rock":
        print("Computer wins!")
    elif human == "Scissors" and computer == "Paper":
        print("You win!")

for counter in entries:
    humanChoice = input("Enter a value of R, P or S: ")
humanDraw = convert(humanChoice)

computerChoice = random.randint(0, 2)
computerDraw = convert(computerChoice)

whoWins(humanDraw, computerDraw)
print("You chose: " + str(humanDraw) + ",  " + "Computer chose: " + str(computerDraw))
