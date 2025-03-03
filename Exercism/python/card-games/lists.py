"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

# Elyse wants to try out a new game called Black Joe. It's similar to Black Jack - where your goal is
# to have the cards in your hand add up to a target value - but in Black Joe the goal is to get the average 
# of the card values to be 7. The average can be found by summing up all the card values and then dividing 
# that sum by the number of cards in the hand.
# Implement a function card_average(<hand>) that will return the average value of a hand of Black Joe.

# >>> card_average([5, 6, 7])
# 6.0
    counting = len(hand)
    total = sum(hand)
    return total / counting

def approx_average_is_average(hand):
    """Return if either of two approximate averages equals the actual average.

    :param hand: list - cards in hand.
    :return: bool - does an approximate average equal the true average?
    """

    true_average = sum(hand) / len(hand)
    
    # Calculate average of first and last card
    sliced_average = (hand[0] + hand[-1]) / 2
    # Get median (middle card)
    median_index = len(hand) // 2
    median = hand[median_index]
    
    if sliced_average == true_average or median == true_average:
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    # Intrigued by the results of her averaging experiment, Elyse is wondering if taking the average of the cards 
    # at the even positions versus the average of the cards at the odd positions would give the same results. 
    # Time for another test function!
    # Implement a function average_even_is_average_odd(<hand>) that returns a Boolean indicating if the average 
    # of the cards at even indexes is the same as the average of the cards at odd indexes.
    # >>> average_even_is_average_odd([1, 2, 3])
    # True
    # >>> average_even_is_average_odd([1, 2, 3, 4])
    # False
    # Get even-indexed and odd-indexed cards
    hand_even = hand[::2]  # Start at 0, step by 2
    hand_odd = hand[1::2]  # Start at 1, step by 2
    
    # Calculate averages
    average_even = sum(hand_even) / len(hand_even) if hand_even else 0
    average_odd = sum(hand_odd) / len(hand_odd) if hand_odd else 0
    
    return average_even == average_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    # Every 11th hand in Black Joe is a bonus hand with a bonus rule: if the last card you draw is a Jack, you double its value.
    # Implement a function maybe_double_last(<hand>) that takes a hand and checks if the last card is a Jack (11). 
    # If the last card is a Jack (11), double its value before returning the hand.
    # >>> hand = [5, 9, 11]
    # >>> maybe_double_last(hand)
    # [5, 9, 22]
    # >>> hand = [5, 9, 10]
    # >>> maybe_do

    if hand[-1] == 11:
        return hand[:-1] + [hand[-1] * 2]
    return list(hand)