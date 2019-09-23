import random
import time


print('Welcome to the Bottega Casino!')

print("The slot machines can take a $0.50, $1.00, or $5.00 bet and payout is: ")
print("3 cherries: JACKPOT! 1:20")
print("2 cherries: 1:10")
print("1 cherry: 1:5")
print("3 spades: 1:5")
print("2 spades: 1:2")
print("3 coins: 1:3")
print("2 coins: 1:1")
print("3 lemons: 1:1")
time.sleep(2)


bet_question = input('Would you like to play slots for a$0.50 b.$1.00 or c.$2.00?')

def find_bet(){
    if bet_question = 'a'{
        return .5
    }
    if bet_question = 'b'{
        return 1
    }
    if bet_question = 'c'{
        return 2
    }
}




items = [
    "Cherries", "Cherries", 
    "Coin", "Coin", "Coin", "Coin", "Coin", "Coin", 
    "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", 
    "Spade", "Spade", "Spade", "Spade", "Spade", 
    ]

def column_one():
    return random.choice(items)

def column_two():
    return random.choice(items)

def column_three():
    return random.choice(items)

result = f'{column_one()} {column_two()} {column_three()}'

print(result)