"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    card_values = {
        'J': 10, 'Q': 10, 'K': 10, 
        'A': 1,
        '2': 2, '3': 3, '4': 4, '5': 5, 
        '6': 6, '7': 7, '8': 8, '9': 9, 
        '10': 10
    }
    return card_values[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one: str - first card dealt in hand.
    :param card_two: str - second card dealt in hand.
    :return: str or tuple - resulting tuple contains both cards if equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    total = value_of_card(card_one) + value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        return 1
    if total > 10:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    is_ace = (
        card_one == 'A' 
        or card_two == 'A'
    )
    is_face_card = (
        value_of_card(card_one) == 10 
        or value_of_card(card_two) == 10
    )
    
    if is_ace and is_face_card:
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    if total == 9 or total == 10 or total == 11:
        return True
    return False
