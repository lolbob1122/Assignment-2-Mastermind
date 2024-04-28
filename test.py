import random

# Generate a random code
code = random.sample(range(1, 6), 4)
print("Code:", code)

# Extract individual digits from the code
c1, c2, c3, c4 = code

# Loop for allowing 10 guesses
for _ in range(10):
    # Take user input for guess
    g = input('Guess a combination of 4 numbers, separated by a space: \n')

    try:
        # Convert input string to list of integers
        guess = [int(x) for x in g.replace(",", " ").split()]
        
        # Check if the length of guess is exactly 4
        if len(guess) != 4:
            print("Please enter exactly 4 numbers separated by spaces.")
            continue  # Skip to the next iteration of the loop
        
        # Check if the guess matches the code
        if guess == code:
            print("Congratulations! You guessed the code correctly!")
            break  # Exit the loop since the code is guessed correctly
        
        # Check if any number in guess is equal to any number in code
        correct_numbers = sum(1 for num in guess if num in code)
        print("Correct numbers:", correct_numbers)
        
        # Optional: Check if the guess contains any numbers in the correct position
        correct_positions = sum(1 for i in range(4) if guess[i] == code[i])
        print("Correct positions:", correct_positions)

        print("Incorrect guess. Try again.")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
