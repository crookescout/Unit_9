# Scout Crooke, 12/05/19, this program plays a game of peace with the user

import card
import deck

my_deck = deck.Deck()
my_deck.shuffle()


def deal_cards(deck):
    """
    this function deals 5 cards each to player 1 and player 2
    :param deck:
    :return: the 5 cards of each player
    """
    cards = []
    for x in range(5):
        my_deck.deal()
        cards.append(my_deck.deal())
    return cards


def compare_cards(card1, card2):
    """
    this function compares each card of player 1 vs. each card of player 2
    :param card1:
    :param card2:
    :return: True or False
    """
    if card1 > card2:
        print("Player 1 won this round")
        return True
    else:
        print("Player 2 won this round")
        return False


def main():
    player_1_score = 0
    player_2_score = 0
    player_1 = deal_cards(my_deck)
    player_2 = deal_cards(my_deck)

    for x in range(5):
        print("This is player 1's card: " + str(player_1[x]))
        print("This is player 2's card: " + str(player_2[x]))
        if compare_cards(player_1[x], player_2[x]):
            player_1_score += 1
        else:
            player_2_score += 1
        print()
    print("This is player 1's score:" + str(player_1_score))
    print("This is player 2's score:" + str(player_2_score))
    if player_1_score > player_2_score:
        print("Player 1 won this game!")
    else:
        print("Player 2 won this game!")


main()
