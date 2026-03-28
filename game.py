#!/usr/bin/env python3
import random

def guess_the_number():
    """A simple number guessing game."""
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            guess = int(input("What's your guess? "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"You got it! It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()