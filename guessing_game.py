
import random

easy = ["apple", "train", "tiger", "money", "india"]
medium = ["python", "bottle", "monkey", "planet", "laptop"]
hard = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy)
elif level == "medium":
    secret = random.choice(medium)
elif level == "hard":
    secret = random.choice(hard)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy)

attempts = 0
print("\nGuess the secret password")
print(f"The secret word has {len(secret)} letters!\n")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

    hint = ""
    for char in guess:
        if char in secret:
            hint += char
        else:
            hint += "-"

    print("Hint:", hint)

print("Game Over")
