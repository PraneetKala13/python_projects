import random

random_numb = random.randint(1, 100)  # Generate a random number
while True:  # Loop until correct number found
    guess_numb = int(input("Guess the number between 1 and 100: "))
    if guess_numb > random_numb:  # Check if higher
        print("Too high!")  # Message sayng number to high
    elif guess_numb < random_numb:  # Check if lower
        print("Too low!")  # m Messaeg if number is too low
    else:
        print("Congratulations! You guess the number")  # Correct number
        break

"""
It's a good idead to add a try catch to ensure users don't use ltters

Here is Mosh's code:

while True:
    try:
        guess = int(input('Guess the number between 1 and 100:'))
    
        if guess < number_to_guess: 
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print(Please enter a valid number')

"""
