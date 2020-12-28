import random

# the game below allows the computer to guess a number that you are thinking of
print("Think of a number 1-100...")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} guess too high (h), too low (l), or correct (c)?: ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed the number you were thinking of. ({guess})")

computer_guess(100)