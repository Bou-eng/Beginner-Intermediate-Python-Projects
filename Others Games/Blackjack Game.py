import random

print("Welcome to BLACKJACK game :)")
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
game = True


def play_again():
    choice = input("Do you wanna play again? ").lower()
    if choice == "no":
        exit()


while game:
    user_game = []
    dealer_game = []
    user_total = 0
    dealer_total = 0


    def calculate_totals(user_game, dealer_game):
        user_total = sum(user_game)
        dealer_total = sum(dealer_game)
        return user_total, dealer_total


    for i in range(2):
        user_game.append(random.choice(cards))
        dealer_game.append(random.choice(cards))
    print(f"You got : {user_game[0]} and {user_game[1]}")
    print(f"Dealer got : {dealer_game[0]}")

    while True:
        user_choice = input("Do you want to hit or stand? ").lower()

        if user_choice == "hit":
            user_game.append(random.choice(cards))
            user_total, dealer_total = calculate_totals(user_game, dealer_game)
            print(f"You got : {user_game[-1]}")
            print(f"Your current total is: {user_total}")

            if user_total > 21:
                print(f"Sorry, you lost! Your total is {user_total}, which is over 21.")
                break

        elif user_choice == "stand":
            print("You chose to stand.")
            break
        else:
            print("Please choose either 'hit' or 'stand'.")

    user_total, dealer_total = calculate_totals(user_game, dealer_game)
    print(f"The second card of the dealer is : {dealer_game[1]}")

    while dealer_total <= 16:
        dealer_game.append(random.choice(cards))
        user_total, dealer_total = calculate_totals(user_game, dealer_game)
        print(f"Dealer drew a card: {dealer_game[-1]}")
        print(f"Dealer's current total is: {dealer_total}")

        if dealer_total > 21:
            print(f"The dealer lost! Dealer's total is {dealer_total}, which is over 21.")
            play_again()
            break

    if dealer_total <= 21:
        print("The dealer stands.")
        user_total, dealer_total = calculate_totals(user_game, dealer_game)
        if dealer_total < user_total <= 21:
            print(f"Congratulations you won!\nYour score is {user_total} and the dealer's is {dealer_total}")
        elif user_total < dealer_total <= 21:
            print(f"Dealer won the game!\nYour score is {user_total} and the dealer's is {dealer_total}")
        elif user_total == dealer_total:
            print(f"It's a tie!\nBoth you and the dealer have {user_total}")

        play_again()
