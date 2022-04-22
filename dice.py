import random
import time

roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "Yes" or roll_again == "Y":
    print("\nRolling the dice...")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The values are:")
    print("Dice 1", dice1, "n\Dice 2 =", dice2)

    if dice1 == dice2:
        print("you rolled a double!")
    else:
        print("Keep trying!")
    roll_again = input("\nRoll the dice again? (Y/N) ")     