import random
from hung_man import word_list
"""heigh = int(input("What is you max heigh : "))
if heigh >= 120 :
    print("You can ride the rollercoaster :)")
    age = int(input("Enter your age : "))
    if age >= 18 :
        print("You have to pay $18")
    else:
        print("We have a special sale for you, you'll pay $7")
else :
    print("You must grow up to 120cm or you will never ride it :(")


<----Checking if a number is odd or even------>
number = int(input("Enter a number : "))
if number % 2 == 0 :
    print(f"The number {number} that you entered is an even number")
else :
    print(f"The number {number} that you entered is an odd number")

# <--------Treasure island---------->
print('''Welcome to the treasure island\nYour mission is to find the treasure.''')
answer = input("Do you wanna start by going left or right ?").lower()
if answer == "right":
    print("You fall into a hole\nGame over :(")
elif answer == "left":
    answer = input("You came across a river do you wanna swim or wait ?").lower()
    if answer == "swim":
        print("You get attacked by a troutt\nGame over :(")
    elif answer == "wait":
        answer = input('''You got across three doors, which one you wanna go
through red, blue or yellow''').lower()
        if answer == "red" :
            print("You got burned by fire\nGame over :( ")
        elif answer == "blue":
            print("You got eaten by beasts\nGame over :(")
        elif answer == "yellow":
            print("Congratulations you won:)")
    else :
            print("Invalid option")
            exit()
else:
    print("Invalid option !\n Game over :(")
#<-------who pays the bill--------->

people = ["********", "*******", "*******", "********", "********", "*******"]
number_of_who_pays = random.randint(0,5)
print(f"The person who will pay is {people[number_of_who_pays]}")
people = ["********", "********", "********", "*********", "*******", "********"]
print("The one who will pay is " + random.choice(people))

#<---------Rock,paper and scisors--------->
rock = '''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''
scissors = '''          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \/
|___/\___|_|___/___/\___/|_|  |___/
'''
paper = '''
 _ __   __ _ _ __    
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|      '''

computer_game = random.randint(1, 3)
valid_options = [1,2,3]
print("1-ROCK\n2-SCISSORS\n3-PAPER")
user_game = int(input("Play using one of the option above"))
if user_game not in valid_options :
    exit()
else :

    if user_game ==1 or computer_game == 1 :
        print(rock)
    if user_game ==2 or computer_game == 2 :
        print(scissors)
    if user_game == 3 or computer_game == 3:
        print(paper)
    if (user_game - computer_game ) %3 ==1 :
        print("Congrats ! You won against the computer")
    elif (user_game - computer_game) %3 == 2:
        print("Sorry but the computer won !")

<------------Generating a random and string password--------->

list_of_alphabets = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"
                     , "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l"
                     , "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r"
                     , "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x"
                     , "Y", "y", "Z", "z"]
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_of_signs = ["!", "@", "#", "$", "%", "&", "/", "(", ")", "*", "^"]
num_of_alpha = int(input("How many Alphabets do you wanna get in your password ?\n"))
num_of_nums = int(input("How many Numbers do you wanna get in your password ?\n"))
num_of_signs = int(input("How many Signs do you wanna get in your password ?\n"))
password = []
for i in range(num_of_alpha):
    password.append(random.choice(list_of_alphabets))
for i in range(num_of_nums):
    password.append(str(random.choice(list_of_numbers)))
for i in range(num_of_signs):
    password.append(random.choice(list_of_signs))
random.shuffle(password)
print("".join(password))


 <----------Hung man Game-------------->

import random

print("Welcome to the hangman game")

# You should replace the following with actual word list and logo imports or definitions
word_list = ["python", "hangman", "programming", "developer"]  # Example word list
game_logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
print(game_logo)

# Initialize the game
secret_word = random.choice(word_list)
guessed_letters = []
remaining_guesses = 7
guessed_word = ["_"] * len(secret_word)

# Game loop
while remaining_guesses > 0 and "".join(guessed_word) != secret_word:
    print(f"Word: {''.join(guessed_word)}")
    print(f"Remaining guesses: {remaining_guesses}")
    user_guess = input("Guess a letter of the secret word: ").lower()

    # Check if the letter has already been guessed
    if user_guess in guessed_letters:
        print("You have already guessed this letter. Try again.")
        continue

    guessed_letters.append(user_guess)

    # Check if the guessed letter is in the secret word
    if user_guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == user_guess:
                guessed_word[i] = user_guess
        print(f"Correct! {user_guess} is in the word.")
    else:
        remaining_guesses -= 1
        print(f"Incorrect! {user_guess} is not in the word.")

    # Print the current state of the word
    print(f"Word: {''.join(guessed_word)}")

# Final results
if "".join(guessed_word) == secret_word:
    print(f"Congratulations! YOU WON THE GAME! The word was: {secret_word}")
else:
    print(f"Sorry, YOU LOST THE GAME. The word was: {secret_word}")  

print("Hello, Welcome to our BID")
winner = ""
highest_price = 0
def find_highest_bid(bidding_dictionary):
    biggest_value = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > biggest_value:
            biggest_value = bid_amount
            winner.append(bidder)
            highest_price.append(biggest_value)


bids = {}
other_person = True
while other_person :
    name = input("Enter your name : ")
    price = int(input("Enter the price : $"))
    bids[name] = price
    should_contunie = input("Is there anyone else who would bid : ").lower()
    if should_contunie == 'no' :
        other_person = False
        find_highest_bid(bids)
    elif should_contunie == "yes":
        print("\n" * 10)
        continue


print(f"The winner is : {winner} with a bid of : ${biggest_value}") """
#  -------------------------
#  |     CALCULATOR        |
#  |------------------------

logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
'''
should_continue = True
while not should_continue:
    num = []
    def calculate(f_num, l_num):
        f_num = float(input("Enter the first number"))
        print('''For Addition---> (+)
                 For Substraction---> (-)
                 For Multiplication---> (*)
                 For Division--->(/)''')
        operator = input("Enter one of the options above : ")
        l_num = float(input("Enter the last number : "))
        if operator == '*':
                num.append({f_num * l_num})
                return f"{f_num} * {l_num} = {f_num * l_num}"
        elif operator == '/':
                num.append({f_num / l_num})
                return f"{f_num} / {l_num} = {f_num / l_num}"
        elif operator == '+':
                num.append({f_num + l_num})
                return f"{f_num} + {l_num} = {f_num + l_num}"
        elif operator == '-':
                num.append({f_num - l_num})
                return f"{f_num} - {l_num} = {f_num - l_num}"
        else:
                return "Invalid option"
    answer = input("Enter yes if you wanna continue using the output: ").lower()
    if answer == 'yes':
        calculate(num, l_num)
    else:
        should_continue = False


