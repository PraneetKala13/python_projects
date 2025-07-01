import random


def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "r" and computer == "s") or \
         (player == "p" and computer == "r") or \
         (player == "s" and computer == "p"):
        return "You win!"
    else:
        return "You lose."


def main():
    choices = {"r": "Rock 🪨", "p": "Paper 📄", "s": "Scissors ✂️"}

    while True:
        player = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()

        if player not in choices:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")
            continue

        computer_choice = random.choice(list(choices))

        print(
            f"You chose {choices[player]}, computer chose {choices[computer_choice]}.")

        result = get_winner(player, computer_choice)
        print(result)

        # Ask to quit after playing a round
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
