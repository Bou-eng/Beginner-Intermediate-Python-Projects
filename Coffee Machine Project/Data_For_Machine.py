resources = {
    milk: 200,
    water: 300,
    coffee: 100,
    sugar: 200,
}
money: 0


def sugar_amount():
    answer = input("How much would you like sugar : (little/medium/alot)").lower()
    if answer == "little":
        return 10
    elif answer == "medium":
        return 20
    elif answer == "alot":
        return 30
    else:
        print("Enter a valid option!")
        sugar_amount()



def machine_off():
    answer = input("Do you want to turn the machine off? : ").lower()
    if answer == "yes":
        return True
    elif answer == "no":
        return False


def print_report():
    print(" ".join(resources) + "\n")


Menu = {
    {
        "Name": "Latte",
        milk_amount: 150,
        water_amount: 200,
        cofee_amount: 24,
        sugar_amount: sugar_amount(),
        "Price": 2.50
    },
    {
        "Name": "Cappuccino",
        milk_amount: 100,
        water_amount: 250,
        cofee_amount: 24,
        sugar_amount: sugar_amount(),
        "Price": 3.75
    },
    {
        "Name": "Expresso",
        milk_amount: 0,
        water_amount: 50,
        cofee_amount: 18,
        sugar_amount: sugar_amount(),
        "Price": 2.20
    }
}
# Money types dictionary
Turkish_Lira = {
    bir_lira: 1,
    elli_kusrus: 50,
    yirmibes_kurus: 25,
    yirmi_kurus: 20
}


def check_resources(answer):
    for i in range(3):
        if milk - Menu[i][answer] >= 0 and water - Menu[i][answer] >= 0 and coffee - Menu[i][answer] >= 0:
            if sugar - Menu[i][answer] >= 0:
                print("Your coffee is about o made")
        else:
            print("Sorry! there is no enough resources to make you coffee")

def calculate_coins():
    global money
    answer = int(input("Enter how many coins are you gonna put in : "))
    for _ in range(answer):
        amount = int(input(f"Enter the {_ + 1}. coins: "))
        money += amount
    return money


def compare_money_price(money_entered):
    if money_entered > money:
        print(f"You entered {money_entered} and you are get a refund of : {money_entered - money}")
    elif money > money_entered:
        print(f"You entered {money_entered} and it's not enough you need to enter : {money - money_entered}")
    else:
        print(f"You entered {money_entered} and you have no refund")

