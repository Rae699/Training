"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param *args: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # APPROACH 1: Procedural Way
    wagons_list = []
    for wagon in args:
        wagons_list.append(wagon)
    return wagons_list

    # APPROACH 2: Pythonic Way (one-liner)
    # return list(args)
    
    # APPROACH 3: Pythonic Way (using unpacking)
    # return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # APPROACH 1: Procedural Way
    # Get first two wagons
    first, second, *rest = each_wagons_id
    
    # Find and remove locomotive (ID 1) from rest
    rest_without_loco = []
    for wagon in rest:
        if wagon != 1:
            rest_without_loco.append(wagon)
        else:
            locomotive = wagon
    
    # Build final list: [1, missing_wagons, rest, first_two]
    return [locomotive] + missing_wagons + rest_without_loco + [first, second]

    # APPROACH 2: Pythonic Way (one-liner)
    # first, second, *rest = each_wagons_id
    # return [1] + missing_wagons + [x for x in rest if x != 1] + [first, second]


def add_missing_stops(route: dict, **kwargs) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param kwargs: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # Step 1: Make a copy of the route
    new_route = route.copy()
    
    # Step 2: Get all values from kwargs
    stops = list(kwargs.values())
    
    # Step 3: Add stops to the new route
    new_route["stops"] = stops
    
    return new_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}
    


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Get all red wagons from first row
    red_wagons = wagons_rows[0]
    
    # Get all blue wagons from second row
    blue_wagons = wagons_rows[1]
    
    # Get all orange wagons from third row
    orange_wagons = wagons_rows[2]
    
    # Make new rows with one of each color
    row1 = [red_wagons[0], blue_wagons[0], orange_wagons[0]]
    row2 = [red_wagons[1], blue_wagons[1], orange_wagons[1]]
    row3 = [red_wagons[2], blue_wagons[2], orange_wagons[2]]
    
    # Return all rows in a list
    return [row1, row2, row3]

