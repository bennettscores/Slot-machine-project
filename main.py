import random
import time
class SlotMachine:

    def __init__(self):
        self.items = [
        "Cherries", "Cherries", 
        "Coin", "Coin", "Coin", "Coin", "Coin", "Coin", 
        "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", 
        "Spade", "Spade", "Spade", "Spade", "Spade", 
        ]
        SlotMachine.main_menu(self)
        self.bet = 0


    def main_menu(self):
        print('Welcome to the Bottega Casino!')

        print("The slot machines can take a $0.50, $1.00, or $5.00 bet and payout is: ")
        print("3 cherries: JACKPOT! 1:20")
        print("2 cherries: 1:10")
        print("3 spades: 1:5")
        print("2 spades: 1:2")
        print("3 coins: 1:3")
        print("2 coins: 1:1")
        print("3 lemons: 1:1.5")

        SlotMachine.asking_bet_question(self)

    def asking_bet_question(self):
        self.bet_question = input('Would you like to play slots for a$0.50 b.$1.00 or c.$2.00?')
        if self.bet_question == 'a' or self.bet_question =='b' or self.bet_question =='c':
            pass
        else:
            print('Please enter "a" for $0.50 "b" for $1.00 or "c" for $2.00')
            self.bet_question
            SlotMachine.asking_bet_question(self)
        SlotMachine.slot_machine(self)

    
    def slot_machine(self):
        column_one = random.choice(self.items)
        column_two = random.choice(self.items)
        column_three = random.choice(self.items)

        result = f'{column_one} {column_two} {column_three}'
        
        
        if result.count("Cherries") == 3:
            print("You won the Jackpot!")
            self.bet = 20
        elif result.count("Cherries") == 2:
            self.bet = 10
        elif result.count ("Spade") == 3:
            self.bet = 5
        elif result.count("Spade") == 2:
            self.bet = 2
        elif result.count("Coin") ==3:
            self.bet = 3
        elif result.count("Coin") == 2:
            self.bet = 1
        elif result.count("Lemon") ==3:
            self.bet = 1.5
        elif result.count("Lemon") ==2:
            self.bet = 0
        
        print(result)
        time.sleep(1)
        SlotMachine.payout_statement(self)


    def payout_statement(self):
        if self.bet_question == 'a':
            winnings = self.bet * .5
        if self.bet_question == 'b':
            winnings = self.bet
        if self.bet_question == 'c':
            winnings = self.bet * 2
        else:
            print('Please enter "a" "b" or "c" for how much you want to bet')

        print(f'You won ${winnings}')
        self.play_again = input("Would you like to play again?")
        SlotMachine.restart(self)


    def restart(self):
        if self.play_again == "yes":
            SlotMachine.main_menu(self)
        elif self.play_again == "y":
            SlotMachine.main_menu(self)
        elif self.play_again == "Yes":
            SlotMachine.main_menu(self)
        elif self.play_again == "Y":
            SlotMachine.main_menu(self)
        elif self.play_again == "no":
            print("Thank you please come again!")
        elif self.play_again == "n":
            print("Thank you please come again!")
        elif self.play_again == "No":
            print("Thank you please come again!")
        else:
            print('Please write yes or no')
            SlotMachine.restart(self)

SlotMachine()