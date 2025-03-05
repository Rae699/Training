"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    coordinate_number = coordinate[0]
    coordinate_letter = coordinate[1]
    return (coordinate_number, coordinate_letter)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    aza_coordinate = convert_coordinate(azara_record[1])
    rui_coordinate = rui_record[1]
    
    print(f"aza_coordinate: {aza_coordinate}, type: {type(aza_coordinate)}")
    print(f"rui_coordinate: {rui_coordinate}, type: {type(rui_coordinate)}")
    
    return aza_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    
    match = compare_records(azara_record, rui_record)
    if not match:
        return "not a match"
    return (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = []
    for record in combined_record_group:
        cleaned_record = (record[0], record[2], record[3], record[4])
        report.append(str(cleaned_record))
    
    return "\n".join(report) + "\n"

    
