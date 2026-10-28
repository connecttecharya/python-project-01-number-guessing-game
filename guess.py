# Number Guessing Game
# My first Python project!
#
# The computer secretly picks a number between 1 and 100,
# and you try to figure out what it is.

import random

# Let the computer pick its secret number
secret_number = random.randint(1, 100)

# We'll count how many guesses it takes
tries = 0

print("Hey there! Let's play a little game.")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Keep asking until the player gets it right
while True:
    guess = input("\nWhat's your guess? ")

    # Oops, that's not a number. Ask again.
    if not guess.isdigit():
        print("Hmm, that doesn't look like a number. Give it another go!")
        continue

    guess = int(guess)
    tries = tries + 1

    if guess < secret_number:
        print("Nope, too low. Go a bit higher!")
    elif guess > secret_number:
        print("Nope, too high. Go a bit lower!")
    else:
        print("You got it! The number was", secret_number)
        print("It took you", tries, "tries. Nice work!")
        break
