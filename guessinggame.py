import random


def random_func():
    return random.randint(1, user_range)


# Var
user_guess = 0

# Input
user_range = int(input("Select range:\n"))
answer = random_func()

while user_guess != answer:
    user_guess = int(input(f"Guess a number from 1 to {user_range}:\n"))
    if user_guess < answer // 2:
        print("Too Low!")
    elif user_guess < answer:
        print("A bit Low!")
    elif user_guess > answer + answer // 2:
        print("Too high!")
    elif user_guess > answer:
        print("A bit high!")

print(f"Good job! The answer is {answer}")
