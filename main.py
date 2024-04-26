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

    code = random.sample(range(1, 6), 4)
    print(code)

    for i in range(10):
        guess = (input('Guess a combination of 4 numbers, separated by a space or a comma: \n')
        print('you have' + int(n) + 'guesses remaining')

        for i in range(len(code)):
            if guess_list[i] == code[i]:
                correct_positions += 1
            elif guess_list[i] in code:
                correct_numbers += 1



    again = input('Would you like to play again? [y/n]:')
    if again == 'y' or 'yes' or  ' ':
        running = True
    else:
        running = False

print('Thank you for playing!')



# Split the input string into a list of elements


# Initialize variables to count correct numbers and correct positions


# Check each number in the user's list


print("Correct numbers:", correct_numbers)
print("Correct positions:", correct_positions)
