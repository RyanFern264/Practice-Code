import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

random_number = random.randint(1, 100)

while attempts > 0:
    print(f"You have {attempts} attempts remaining in order to guess the number")
    guess = int(input("Make a guess: "))
    print(f" its {random_number} btw")
    if guess > random_number:
        print("Too high.\n Guess again.")
        attempts -= 1
    elif guess < random_number:
        print("Too low.\n Guess again.")
        attempts -= 1
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}")
        attempts = 0
