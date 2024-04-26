# Generate Sample
# Ask for input
# Give feedack up to 10 times (correct position or correct number)
# Win condition if correct sample guessed
import random
from typing import List, Any

running = True
while running:

    print('*** Codebreaking Mastermind game ***'
    '\nI have a code with 4 colours, each different. Each colour is'
    '\nrepresented by a number 1 - 6, as there are 6 possible colours in total.'
    '\n\nAttempt to guess the code within 10 times using my score of your guess.')

    # Generate a random code
    code = random.sample(range(1, 6), 4)
    print("Code:", code)

    # Extract individual digits from the code
    c1, c2, c3, c4 = code

    # Loop for allowing 10 guesses
    for _ in range(10):
        # Take user input for guess
        g = input('Guess a combination of 4 numbers, separated by a comma or a space: \n')

        try:
            # Convert input string to list of integers
            guess = [int(x) for x in g.replace(",", " ").split()]

            # Check if the length of guess is exactly 4
            if len(guess) != 4:
                print("Please enter exactly 4 numbers separated by spaces.")
                continue  # Skip to the next iteration of the loop

            g1, g2, g3, g4 = guess
            for i in range(4):
                if guess.index(code[i]) == code.index(code[i]):
                    check = True
            if check == True:
                print('A digit is correct and in the right place')
            else:
                    print('Incorrect, try again.')
                    print(code[i])

        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")



    again = input('Would you like to play again? [y/n]:')
    if again == 'y' or 'yes' or ' ':
        running = True
    else:
        running = False

print('Thank you for playing!')



