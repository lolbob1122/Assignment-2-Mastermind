import random

running = True
while running:

    print('*** Codebreaking Mastermind game ***'
    '\nI have a code with 4 colours, each different. Each colour is'
    '\nrepresented by a number 1 - 6, as there are 6 possible colours in total.'
    '\n\nAttempt to guess the code within 10 times using my score of your guess.')

    # Generate a random code
    code = random.sample(range(1, 6), 4)
    print("\n Code:", code, '\n') # print for debug

    # Loop for allowing 10 guesses
    attempts = 10
    while attempts > 0:
        # Take user input for guess
        if attempts < 10:
            g = input('Guess a combination of 4 digits, separated by a comma or a space: \n')
        else:
            g = input('Please guess another combination of 4 numbers, separated by a comma or a space: \n')
        try:
            # Convert input string to list of integers
            guess = [int(x) for x in g.replace(",", " ").split()]

            ### print("\n Guess:", guess, "Length of guess:", len(guess), '\n')  ### Debugging print statement
            # Check if the length of guess is exactly 4
            if len(guess) != 4: 
                print("/n Please only enter exactly 4 numbers separated by commas or spaces. /n")
                continue  # Skip to the next iteration of the loop

            #checks for how many are already correct and in the right place
            correct_count = sum(1 for i in range(4) if guess[i]==code[i])
            #check for correct out of position (oop_correct) numbers
            oop_correct = sum(1 for num in guess if num in code) - correct_count
            if correct_count == 4:
                print("You won!")
                
                break
            elif correct_count > 0 or oop_correct > 0:
                print(correct_count, "digit(s) is(are) correct and in the right place \n", 
                oop_correct, "other(s) is(are) correct but in the wrong place")

            else:
                print('Incorrect, try again.')
                
            attempts = attempts - 1 
            if  attempts > 0:
                print("You have ", attempts, "guesses remaining. \n")
            else:
                print("You Lost!")
        except ValueError:
            print("Invalid input. Please enter digits separated by spaces or commas.")



    again = input('Would you like to play again? [y/n]:')
    # if again == "n" or again == "no":
    #     running = False
    if again == 'y' or again == 'yes' or again == "\n":
        running = True
    else:
        running = False

print('Thank you for playing!')



