import random

number_to_guess = random.randint(1, 100)
guess = 0
def game():
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    if guess < number_to_guess:
        print("Too low!")
        game()
    elif guess > number_to_guess:
        print("Too high!")
        game()
    else:
        print("Congratulations! You've guessed the number.")

game()