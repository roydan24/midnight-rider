# main.py
# Midnight Rider
# Text-based adventure game
# Gamespot gives it 9 out of 10

import sys
import textwrap
import time


INTRODUCTION =  """
WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME. 
THE CAR IS SPECIAL.

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GON GETCHU

-------
"""

CHOICES = """
    ----
    Q. QUIT
    ----
"""

def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

    def main():
        intro()

    # Variables
    done = False

    # MAIN LOOP
    while not done:
        pass
        # TODO: Check if reached END GAME

        # Present the user their choices
        print(CHOICES)

        user_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if user_choice == "q":
            done = True

        # TODO: Present the user their choices

        # TODO: Change the environment based on
        #       user choice, and RNG
        # TODO: random event generator

    # Outro
    print("Thanks for playing")


if __name__ == "__main__":
    main()