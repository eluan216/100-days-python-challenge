import random

secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to my python guessing game!")
print("Guess a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")