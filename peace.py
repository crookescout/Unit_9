# Scout Crooke, 12/05/19, this program plays a game of peace with the user

import deck


def deal_cards(my_deck):
    """
    this function deals 5 cards each to player 1 and player 2
    :param my_deck:
    :return: a list of 5 cards of each player
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
    :return: True if player 1 won or False if player 2 won
    """
    if card1 > card2:
        print("Player 1 won this round")
        return True
    else:
        print("Player 2 won this round")
        return False


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()

    # this sets each player's beginning score to 0
    player_1_score = 0
    player_2_score = 0

    # this deals the cards to each player
    player_1 = deal_cards(my_deck)
    player_2 = deal_cards(my_deck)

    for x in range(5):
        # this prints out each players card and compares them
        print("This is player 1's card: " + str(player_1[x]))
        print("This is player 2's card: " + str(player_2[x]))
        if compare_cards(player_1[x], player_2[x]):
            player_1_score += 1
        else:
            player_2_score += 1
        print()

    # this adds points to each player's score depending on if they won the round
    print("This is player 1's score:" + str(player_1_score))
    print("This is player 2's score:" + str(player_2_score))

    # this determines which player won the game based on their scores
    if player_1_score > player_2_score:
        print("Player 1 won this game!")
    else:
        print("Player 2 won this game!")


main()
