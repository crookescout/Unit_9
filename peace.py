# Scout Crooke, 12/05/19, this program plays a game of peace with the user

import card
import deck

my_deck = deck.Deck()
my_deck.shuffle()


def deal_cards(deck):
    cards = []
    for x in range(5):
        my_deck.deal()
        cards.append(my_deck.deal())
    return cards


def main():
    player_1 = deal_cards(my_deck)
    print("These are player 1's cards:")
    for x in player_1:
        print(x)
    player_2 = deal_cards(my_deck)
    print("These are player 2's cards:")
    for x in player_2:
        print(x)


def compare_cards(card1, card2):
    card1 = player_1[1]
    card2 = player_2[2]
    player_1_score = 0
    player_2_score = 0
    if card1 > card2:
        print("player 1 won this round")
        player_1_score += 1
    else:
        print("player 2 won this round")
        player_2_score += 1

main()
