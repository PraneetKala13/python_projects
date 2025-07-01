import random

random_numb = random.randint(1, 100)  # Generate a random number
while True:  # Loop until correct number found
    # Ask for number
    guess_numb = int(input("Guess the number between 1 and 100: "))
    if guess_numb > random_numb:  # Check if higher
        print("Too high!")  # Message sayng number to high
    elif guess_numb < random_numb:  # Check if lower
        print("Too low!")  # m Messaeg if number is too low
    else:
        print("Congratulations! You guess the number")  # Correct number
        break
