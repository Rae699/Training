"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    # Elyse is really looking forward to playing some poker (and other card games) during her upcoming trip to Vegas. 
    # Being a big fan of "self-tracking" she wants to put together some small functions that will help her with tracking tasks and has asked for your help thinking them through.
    # Elyse is especially fond of poker, and wants to track how many rounds she plays - and which rounds those are. 
    # Every round has its own number, and every table shows the round number currently being played. 
    # Elyse chooses a table and sits down to play her first round. She plans on playing three rounds.
    # Implement a function get_rounds(<round_number>) that takes the current round number and returns a single list with that round and the next two that are coming up:
    # >>> get_rounds(27)
    # [27, 28, 29]

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

    total = sum(hand)
    count = len(hand)
    return float(total / count)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # Step 1: Access the first and last item and store their value in a variable
    first = hand[0]
    last = hand[-1]
    
    # Step 2: Access the median then stores it
    median_index = len(hand) // 2
    
    # Step 3: Count the number of cards dynamically in step 1
    # Reminder that len can only take an int value, not a range (range(len())
    count = 2
    
    # Step 4: Get all the averages and the median
    true_average = card_average(hand)
    first_last_average = (first + last) / count
    median = hand[median_index]
 
    return first_last_average == true_average or median == true_average
     



def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    cards_even = hand[::2]
    cards_odd = hand[1::2]
    total_even = sum(cards_even)
    total_odd = sum(cards_odd)
    count_even = len(cards_even)
    count_odd = len(cards_odd)
    
    average_even = total_even / count_even
    average_odd = total_odd / count_odd
    
    return average_even == average_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    # Needs:
    #   1. Access the last card in the hand
    #   2. Get its value and compare it to 11
    #   3. if value is 11, double it, else do nothing
    #   4. Return the new list with the value of the last card edited

    # Make a copy iof the current list so we can change items without altering things on the initial list
    new_hand = hand.copy()
    
    if new_hand[-1] == 11:
        new_hand.remove(11)
        new_hand.append(11 * 2)
    return new_hand


