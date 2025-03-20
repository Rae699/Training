"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param *args: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_wagon, second_wagon, locomotive, *remaining_wagons = each_wagons_id
    return [locomotive] + missing_wagons + remaining_wagons + [first_wagon, second_wagon]


def add_missing_stops(route: dict, **kwargs) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param kwargs: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # Create a copy of the original route dict
    updated_route = route.copy()
    
    # Sort the stops by their keys and extract the values
    sorted_stops = [value for _, value in sorted(kwargs.items())]
    
    # Add stops to the updated route: Stops become the key and sorted stops becomes the value (a list of all the stops)
    updated_route["stops"] = sorted_stops
    
    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    extended_route = {**route, **more_route_information}
    return extended_route
    

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Transpose the matrix - convert rows to columns
    result = []
    for column in zip(*wagons_rows):
        result.append(list(column))
    return result



