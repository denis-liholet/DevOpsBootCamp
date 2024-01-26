# Make a game of rock, paper scissors against the computer.
# Algorithm:
# -	Tell user to enter either rock,paper or scissors
# -	Get the response
# -	Generate a random number from 1 to 3 (1=rock, 2=paper, 3=scissors)
# -	Compare user selection and computer selection
# -	Display who wins.
# Extend the previous program to:
# -	Make sure the user enters a valid entry.
# -	Add a loop structure to play several times and keep a running score
# -	Make a suitable variable type to store choices.

from random import choice

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
CHOICES = [ROCK, PAPER, SCISSORS]
CHOICE_PHRASE = "Please enter 'Rock', 'Paper' or 'Scissors'"
RESULTS = []


def get_ai_choice() -> str:
    return choice(CHOICES)


def get_user_choice() -> str:
    user_choice = input(f"{CHOICE_PHRASE}: ").lower()
    if user_choice not in CHOICES:
        return "Error, incorrect choice."
    return user_choice


def get_result(user_choice, ai_choice) -> int:
    if user_choice == ai_choice:
        return -1
    elif (user_choice == 'rock' and ai_choice == 'scissors') or \
            (user_choice == 'paper' and ai_choice == 'rock') or \
            (user_choice == 'scissors' and ai_choice == 'paper'):
        return 1
    else:
        return 0


def game_results() -> str:
    res_dict = {i: RESULTS.count(i) for i in RESULTS}
    return f"Games played: {len(RESULTS)}, " \
           f"you won {res_dict.get(1, 0)} times, the AI won {res_dict.get(0, 0)}, " \
           f"draws: {res_dict.get(-1, 0)}"


if __name__ == "__main__":
    while True:
        user = get_user_choice()
        if 'Error' in user:
            print(user)
            continue
        print(f"You chose: {user.upper()}")
        ai = get_ai_choice()
        print(f"AI chose: {ai.upper()}")
        winner = get_result(user_choice=user, ai_choice=ai)
        if winner == 0:
            print("AI wins!")
        elif winner == 1:
            print("You win!")
        else:
            print("It's a tie!")
        RESULTS.append(winner)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(game_results())
            print("Thanks for playing! Goodbye.")
            break
        print("\n------------------------------\n")
