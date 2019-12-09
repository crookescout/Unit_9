class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif other.rank > self.rank:
            return False
        else:
            order = ["Clubs", "Diamonds", "Hearts", "Spades"]
            score_1 = order.index(self.suit)
            score_2 = order.index(other.suit)
            if score_1 > score_2:
                return True
            else:
                return False

    def __str__(self):
        values = ["Ace", "Two", "Three", "Four", "Five", "Six",
                  "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        return values[self.rank - 1] + " of " + str(self.suit)
