import random
import time

def main_menu():
    print('Welcome to the Bottega Casino!')

    print("The slot machines can take a $0.50, $1.00, or $5.00 bet and payout is: ")
    print("3 cherries: JACKPOT! 1:20")
    print("2 cherries: 1:10")
    print("3 spades: 1:5")
    print("2 spades: 1:2")
    print("3 coins: 1:3")
    print("2 coins: 1:1")
    print("3 lemons: 1:1.5")
    time.sleep(2)


    bet_question = input('Would you like to play slots for a$0.50 b.$1.00 or c.$2.00?')
    slot_machine()

def find_bet():
    if bet_question == 'a':
        return .5
    
    if bet_question == 'b':
        return 1
    
    if bet_question == 'c':
        return 2
    

items = [
    "Cherries", "Cherries", 
    "Coin", "Coin", "Coin", "Coin", "Coin", "Coin", 
    "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", 
    "Spade", "Spade", "Spade", "Spade", "Spade", 
    ]
def slot_machine():
    column_one = random.choice(items)
    column_two = random.choice(items)
    column_three = random.choice(items)

    result = f'{column_one} {column_two} {column_three}'
    return result
    payout()



def payout():
    if result.count("Cherries") == 3:
        print("You won the Jackpot!")
        return 20
    elif result.count("Cherries") == 2:
        return 10
    elif result.count ("Spade") == 3:
        return 5
    elif result.count("Spade") == 2:
        return 2
    elif result.count("Coin") ==3:
        return 3
    elif result.count("Coin") == 2:
        return 1
    elif result.count("Lemon") ==3:
        return 1.5
    elif result.count("Lemon") ==2:
        return 0
    winnings = payout() * find_bet()
    print(f'You won ${winnings}')
    play_again =input("Would you like to play again?")
    restart()

def restart():
    if play_again == "yes":
        main_menu()
    elif play_again == "y":
        main_menu
    elif play_again == "Yes":
        main_menu()
    elif play_again == "Y":
        main_menu
    elif play_again == "no":
        print("Thank you please come again!")
    elif play_again == "n":
        print("Thank you please come again!")
    elif play_again == "No":
        print("Thank you please come again!")
    elif play_again == "N":
        print("Thank you please come again!")

main_menu()