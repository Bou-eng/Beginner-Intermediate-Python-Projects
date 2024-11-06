import random

game_over = False

def play_again():
    answer = input("Do you want to play again? (yes/no): ").lower()
    if answer == "yes":
        return True
    elif answer == "no":
        return False


def compare_function(guessed_number, random_number, attempts):
    if guessed_number > random_number:
        print("Too high.")
    elif guessed_number < random_number:
        print("Too low.")
    else:
        print(f"Congrats! You guessed the number {random_number} correctly.")
        return True
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")
    return attempts

while not game_over:
    random_number = random.randint(1, 100)
    print("\nWelcome To the Number Guessing Game :)")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose the difficulty: type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid option, select one of the options given.")
        continue  #

    game_won = False
    while attempts > 0 and not game_won:
        guess = int(input("Make a guess: "))
        result = compare_function(guess, random_number, attempts)

        if result == True:
            game_won = True
            break
        else:
            attempts = result

        if attempts == 0:
            print(f"You ran out of attempts. The correct number was {random_number}.")
    game_over = not play_again()
