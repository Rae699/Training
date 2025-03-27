"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    
    letters = ['A', 'B', 'C', 'D']
    for letter in range(number):
        yield letters[letter % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    
    letters = ['A', 'B', 'C', 'D']
    for seat in range(number):
        # Calculate base row number
        base_row = (seat // 4) + 1
        # Adjust for row 13
        if base_row >= 13:
            base_row += 1
        letter = letters[seat % 4]
        yield f"{base_row}{letter}"


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))
    passenger_seat = {}
    
    for passenger in passengers:
        passenger_seat[passenger] = next(seats)
    
    return passenger_seat


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    TICKET_LENGTH = 12
    
    for seat in seat_numbers:
        # Create the base ticket code (seat + flight_id)
        base_code = f"{seat}{flight_id}"
        # Calculate how many zeros we need to add
        padding_length = TICKET_LENGTH - len(base_code)
        # Create the padding of zeros
        padding = '0' * padding_length
        # Yield the complete ticket code
        yield f"{base_code}{padding}"