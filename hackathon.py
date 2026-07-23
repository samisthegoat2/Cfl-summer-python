import random  # Import the random module first

def number_guessing_game():
    print(" Welcome to the Number Guessing Game!")
    ...
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        

        if guess < 1 or guess > 100:
            print(" Please guess a number between 1 and 100.")
            continue

        if guess < secret_number:
            print(" Too low! Try again.")
            attempts += 1
        elif guess > secret_number:
            print(" Too high! Try again.")
            attempts += 1
        else:
            print(f" Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break

        if attempts == 7:
            print("you ran out of Attempts.")
            break
number_guessing_game()
      
