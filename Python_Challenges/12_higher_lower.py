# Write a program for a Higher / Lower guessing game:
# -	The computer randomly generates a sequence of up to 10 numbers between 1 and 13.
#   The player each after seeing each number in turn has to decide whether the next number is higher or lower.
# -	If you get 10 guesses right you win the game.
# Example:
# >Starting number : 12
# >Higher(H) or lower(L)? L
# >Next number 8
# >Higher(H) or lower(L)? L
# >Next number 11
# >You lose

from random import sample


fail_msg = "You lose..."
win_msg = "You win!!!"
upper_limit = 14
list_len = 10
numbers = sample(range(1, upper_limit), list_len)


def game_handler(answer, current, previous):
    match answer:
        case 'H':
            if current > previous:
                return True
        case 'L':
            if current < previous:
                return True
        case _:
            print("Oops! Something's wrong...")
            exit(0)
    return False


def check_loop_end(counter):
    if counter == list_len - 1:
        print(win_msg)
        exit(0)


print(f"Starting number: {numbers[0]}")
for i in range(1, list_len):
    user_input = input("Next number: higher(h) or lower(l)? ").upper()
    current_num = numbers[i]
    previous_num = numbers[i - 1]
    print(f"Next number: {current_num}")
    right_answer = game_handler(user_input, current_num, previous_num)
    if not right_answer:
        print(fail_msg)
        break
    check_loop_end(counter=i)
