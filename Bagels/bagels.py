"""Bagels is a deductive logic game Where you must guess a number based on clues"""

import random
import string

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("""Bagels a deductive logic game
        I am thinking of a {}-digit number with no reppeated digits
        Try to guess waht number it is
        Here are some clues
        When I say:     That means:
        Pico            One digit is correct but in the wrong position
        fermi           One digit is correct and in the right position
        Bagels          No digit is correct
        
        For example if the secret number was 248 and your guess was 843,
        the clues would be Fermi Pico""".format(NUM_DIGITS))

    while True:  # Main game loop
        secret_num = get_secret_num()
        print("I am thinking of a number")
        print("You have {} guesses to get it".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until a valid guess is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_guesses))
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was {}".format(secret_num))

        # Ask player if they want to play again
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


def get_secret_num():
    numbers = list('0123456789')  # create a list of digits 0-9
    random.shuffle(numbers)
    secret_num = ''
    # secret_num = str(random.randint(100,1000))

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all
    else:
        # sort the clues into alphabetical order
        # so their original order doesn't give information anyways
        # clues.sort()
        # make a single string from the list of string clues
        return " ".join(clues)


# if program is run instead of imported run the game:
if __name__ == '__main__':
    main()
