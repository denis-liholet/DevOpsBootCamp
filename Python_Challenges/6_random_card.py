# Write a program that will generate a random playing card e.g. ‘9 Hearts’,
# ‘Queen Spades’ when a key is pressed.

from random import randint


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cards = ["Ace", "Two", "Three", "Four", "Five", "Six",
         "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

print("To get new card: press any key + 'Enter'. To exit, press 'q' + 'Enter'\n")
while True:
    card_type = randint(0, 12)
    suit_type = randint(0, 3)
    print(f"{cards[card_type]} {suits[suit_type]}")
    key = input("")
    if key. lower () == "q":
        break
