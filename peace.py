# Scout Crooke, 12/05/19, this program plays a game of peace with the user

import card
import deck

my_deck = deck.Deck()
my_deck.shuffle()


def deal_cards(deck):
    cards = []
    for x in range(5):
        cards.deal(card)
