from Data_Of_Cities import logo
from Data_Of_Cities import cities_population
import random

print(f"Welcome to our game : \n{logo}\n ")

game_over = False
score = 0  # Move score outside the function to track it across multiple rounds


def quit_the_game():
    answer = input("Do you wanna continue? (yes/no): ").lower()
    if answer == "yes":
        return False
    elif answer == "no":
        return True
    else:
        print("Please enter a valid answer.")
        return quit_the_game()  # Keep asking if invalid input


def compare(one, two):
    if one > two:
        return one
    elif one < two:
        return two


def pick_two_cities():
    global game_over, score  # Access score and game_over from the outer scope
    city = []

    # Pick two unique cities
    for _ in range(2):
        city.append(random.choice(cities_population))
    if city[0] == city[1]:
        while True:
            city[1] = random.choice(cities_population)
            if city[0] != city[1]:
                break

    print(f"City A: {city[0]['City']} - Population: {city[0]['Population']}")
    print(f"City B: {city[1]['City']}")

    # Ask the user for their guess
    answer = input("Which city has the higher population? A or B: ").upper()

    # Compare populations
    check = compare(city[0]["Population"], city[1]["Population"])
    if check == city[0]["Population"] and answer == "A":
        print("You got it!")
        score += 1
        game_over = quit_the_game()
        if game_over:
            print(f"Your final score is {score}")
    elif check == city[1]["Population"] and answer == "B":
        print("You got it!")
        score += 1
        game_over = quit_the_game()
        if game_over:
            print(f"Your final score is {score}")
    else:
        print("You didn't get it!")
        print(f"Your final score is {score}")
        game_over = quit_the_game()
        score = 0

while not game_over:
    pick_two_cities()
