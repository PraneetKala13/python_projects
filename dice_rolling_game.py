import math
import random

check = "y"
while check != "n":
    check = input("Roll the dice? (y/n):")  # Ask use if they want to roll dice
    if check == "y":  # Check if the response is valid
        random1 = random.randint(1, 6)  # Generate first random number
        random2 = random.randint(1, 6)  # Generate second random number
        print(f"({random1}, {random2})")  # Display the numebr
    else:
        print("Invalid choice")  # Message for invalid choice
print("Thanks for playing")  # Message for ending the game
