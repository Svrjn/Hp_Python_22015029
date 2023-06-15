import random

while True:
    command = input("Enter a command (toss/quit): ")
    if command == "toss":
        dice_roll = random.randint(1,6)
        print("Your Dice roll is:", dice_roll)
    elif command == "quit":
        break
    else:
        print("Invalid command, try again.")