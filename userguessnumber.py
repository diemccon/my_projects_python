import random

# the game below allows you to guess a number that the computer has randomly generated

print("Try to guess a number 1-100 that the computer has randomly generated...")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("Not quite. Your guess was too low. ")
        elif guess > random_number:
            print("Not quite. Your guess was too high.")

    print(f"Yay! You guessed the number correct. ({random_number}) ")

guess(100)