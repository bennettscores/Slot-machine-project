import random


print('Welcome to the Bottega Casino! Would you like to play slots for $0.50, $1.00, or $5.00')

items = ["Coin", "Lemon", "Diamond", "Spade", "Club", "Heart", "King"]


def column_one():
    return random.choice(items)
    
print(column_one())