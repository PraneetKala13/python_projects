import math
import random

check = "y"
while check != "n":
    check = input("Roll the dice? (y/n):")
    if check == "y":
        random1 = random.randint(1, 6)
        random2 = random.randint(1, 6)
        print(f"({random1}, {random2})")
    else:
        print("Invalid choice")
print("Thanks for playing")
