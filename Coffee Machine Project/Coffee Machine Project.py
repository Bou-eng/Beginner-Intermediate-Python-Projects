import random

# Resources available in the machine
resources = {
    "milk": 200,
    "water": 300,
    "coffee": 100,
    "sugar": 200,
}

# Starting money in the machine
money = 0

# Coffee menu with resource requirements and prices
Menu = [
    {
        "Name": "Latte",
        "milk_amount": 150,
        "water_amount": 200,
        "coffee_amount": 24,
        "Price": 2.50
    },
    {
        "Name": "Cappuccino",
        "milk_amount": 100,
        "water_amount": 250,
        "coffee_amount": 24,
        "Price": 3.75
    },
    {
        "Name": "Espresso",
        "milk_amount": 0,
        "water_amount": 50,
        "coffee_amount": 18,
        "Price": 2.20
    }
]

# Valid Turkish Lira coins
Turkish_Lira = {
    "bir_lira": 1,
    "elli_kurus": 0.50,
    "yirmibes_kurus": 0.25,
    "yirmi_kurus": 0.20
}

# Function to ask for sugar amount
def sugar_amount():
    while True:  # Loop until a valid response is given
        response = input("How much sugar would you like: (little/medium/alot)? ").lower()
        if response == "little":
            return 10
        elif response == "medium":
            return 20
        elif response == "alot":
            return 30
        else:
            print("Enter a valid option!")

# Function to print the report of the current resources
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Sugar: {resources['sugar']}g")
    print(f"Money: {money} TL")

# Function to turn off the machine
def machine_off():
    response = input("Do you want to turn off the machine? (yes/no): ").lower()
    return response == "yes"

# Function to check if there are enough resources for the drink
def check_resources(drink_index, sugar_amount):
    drink = Menu[drink_index]
    if resources["milk"] >= drink["milk_amount"] and resources["water"] >= drink["water_amount"] and resources["coffee"] >= drink["coffee_amount"]:
        if resources["sugar"] >= sugar_amount:
            return True
        else:
            print("Not enough sugar!")
    else:
        print("Sorry, there are not enough resources to make your coffee.")
    return False

# Function to calculate the coins inserted by the user
def calculate_coins():
    total = 0
    num_coins = int(input("Enter how many coins you are going to put in: "))
    for i in range(num_coins):
        amount = float(input(f"Enter the value of coin {i + 1} (1, 0.50, 0.25, 0.20): "))
        if amount in [1, 0.50, 0.25, 0.20]:
            total += amount
        else:
            print("Invalid coin value! Try again.")
            return calculate_coins()  # Retry if invalid coin is inserted
    return total

# Function to compare the total coins entered with the drink price
def compare_money_price(total_money, drink_price):
    if total_money >= drink_price:
        change = total_money - drink_price
        print(f"You entered {total_money} TL. Your change is: {round(change, 2)} TL")
        return True
    else:
        print(f"You entered {total_money} TL, which is not enough. You need {round(drink_price - total_money, 2)} TL more.")
        return False

# Function to make the coffee by deducting the required resources
def make_coffee(drink_index, sugar_amount):
    drink = Menu[drink_index]
    resources["milk"] -= drink["milk_amount"]
    resources["water"] -= drink["water_amount"]
    resources["coffee"] -= drink["coffee_amount"]
    resources["sugar"] -= sugar_amount
    global money
    money += drink["Price"]
    print(f"Your {drink['Name']} with {sugar_amount}g of sugar is ready!")

# Main process function to handle the flow of making a coffee
def process(drink_index):
    sugar = sugar_amount()  # Get sugar preference
    if check_resources(drink_index, sugar):  # Check if enough resources
        total_money = calculate_coins()  # Ask for coins
        if compare_money_price(total_money, Menu[drink_index]["Price"]):  # Check if money is enough
            make_coffee(drink_index, sugar)  # Make the coffee
        else:
            print("Money refunded.")

# Main loop to run the coffee machine
done = False
while not done:
    answer = input("What would you like? (1.Latte/2.Cappuccino/3.Espresso/report/off): ").lower()
    if answer == "1" or answer == "latte":
        process(0)  # Latte
    elif answer == "2" or answer == "cappuccino":
        process(1)  # Cappuccino
    elif answer == "3" or answer == "espresso":
        process(2)  # Espresso
    elif answer == "report":
        print_report()
    elif answer == "off":
        done = machine_off()
    else:
        print("Please enter a valid option!")
