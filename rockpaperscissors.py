import random

# This is a very simple rock, paper, scissors game.

# In the future, I could add feedback for the player if they lose...
# For example, if player chooses paper and the computer chooses scissors, let the player know that the reason why they
# lost is because the computer's choice of scissors defeated their choice of paper. (And so on an so forth...)
# I could also loop the game to continue playing until the player wins. (Restarts game after loss or tie)


def play():
    user = input("Press 'r' for rock. Press 'p' for paper. Press 's' for scissors.\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie. "

    if is_win(user, computer):
        return "You won!"

    return "You lost."

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "s") or (player == "p" and opponent == "r"):
        return True

print(play())