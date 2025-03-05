"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

# Implement the create_inventory(<input list>) function that creates an "inventory" from an input list of items. 
# It should return a dict containing each item name paired with their respective quantity.
# >>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
# {"coal":1, "wood":2, "diamond":3}

    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

# Implement the add_items(<inventory dict>, <item list>) function that adds a list of items to the passed-in inventory:
# >>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
# {"coal":2, "wood":2, "iron":1}

    for i in items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

# Implement the decrement_items(<inventory dict>, <items list>) function that takes a list of items. 
# Your function should remove 1 from an item count for each time that item appears on the list:
# >>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
# {"coal":2, "diamond":0, "iron":3}
# Item counts in the inventory should not be allowed to fall below 0. If the number of times an item 
# appears on the input list exceeds the count available, the quantity listed for that item should remain at 0.
# Additional requests for removing counts should be ignored once the count falls to zero.
# >>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
# {"coal":0, "wood":0, "diamond":1}

    for i in items:
        if i in inventory:
            if inventory[i] > 0:
                inventory[i] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

# Implement the remove_item(<inventory dict>, <item>) function that removes an item and its count entirely from an inventory:
# >>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
# {"wood":1, "diamond":2}
# If the item is not found in the inventory, the function should return the original inventory unchanged.
# >>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
# {"coal":2, "wood":1, "diamond":2}

    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    result = []
    for item, count in inventory.items():
        if count > 0:
            result.append((item, count))
    return result 

    