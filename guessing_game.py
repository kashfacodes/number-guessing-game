import random

while True:

    print("Welcome to the Number Guessing Game!")

    print("\nChoose your difficulty:")
    print("1. Easy   - 1 to 50, 10 attempts")
    print("2. Medium - 1 to 100, 7 attempts")
    print("3. Hard   - 1 to 500, 5 attempts")

    difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == "1":
        max_number = 50
        max_attempts = 10

    elif difficulty == "2":
        max_number = 100
        max_attempts = 7

    elif difficulty == "3":
        max_number = 500
        max_attempts = 5

    else:
        print("Invalid choice. Starting Medium mode.")
        max_number = 100
        max_attempts = 7

    secret_number = random.randint(1, max_number)
    attempts = 0

    while attempts < max_attempts:

        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"You got it in {attempts} attempts! 🎉")
            break

        elif guess < secret_number:
            print("Too low!")

        else:
            print("Too high!")

    if attempts == max_attempts and guess != secret_number:
        print(f"Game over! The number was {secret_number}.")

    play_again = input("Play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing! 👋")
        break