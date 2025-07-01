import random

# This function will compare results and choose a winner


def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "r" and computer == "s") or \
         (player == "p" and computer == "r") or \
         (player == "s" and computer == "p"):
        return "You win!"
    else:
        return "You lose."

# This is the main function that does most of the work


def main():
    choices = {"r": "Rock 🪨", "p": "Paper 📄", "s": "Scissors ✂️"}

    while True:
        player = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()

        # Check if the entry is valid or not
        if player not in choices:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")
            continue

        # Computer to randomnly select their choice
        computer_choice = random.choice(list(choices))

        print(
            f"You chose {choices[player]}, computer chose {choices[computer_choice]}.")

        # Call to function to find winner after selections are made
        result = get_winner(player, computer_choice)
        print(result)

        # Ask to quit after playing a round
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()


"""


Add Mosh's code:
import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():
  while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice in choices:
      return user_choice      
    else:
      print('Invalid choice!')
      
def display_choices(user_choice, computer_choice):
  print(f'You chose {emojis[user_choice]}')
  print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print('Tie!')
  elif (
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == ROCK)):
    print('You win')
  else:
    print('You lose')  

def play_game():
  while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    display_choices(user_choice, computer_choice)

    determine_winner(user_choice, computer_choice)

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
      break

play_game()

"""
