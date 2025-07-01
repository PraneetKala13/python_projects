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

"""
Could make it robust and check for uppercase and lowercase
Ensure that the entered string character always changes to lowercase
Don't use the same variable "check" in the start, use a Boolean

Mosh's final code
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice := 'y': ==
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')

"""
