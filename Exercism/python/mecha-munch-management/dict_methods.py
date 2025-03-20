"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart 


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    
    inventory_from_notes = {}
    return inventory_from_notes.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    
    fulfillment_cart = {}
    
    for key in cart.keys():
        if key in aisle_mapping:
            fulfillment_cart[key] = [cart[key]] + aisle_mapping[key]    

    reversed_order_cart = dict(sorted(fulfillment_cart.items(), reverse=True))
    return reversed_order_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store. {item: [quantity, aisle, bool]}
    :param store_inventory: dict - store available inventory {item: [quantity, aisle, bool]}
    :return: dict - store_inventory updated.
    """

    updated_inventory = store_inventory.copy()
    
    for item, details in fulfillment_cart.items():
        if item in updated_inventory:
            # Get order quantity from fulfillment cart (first element of the details list)
            order_quantity = details[0]
            # Get current inventory quantity (first element of the inventory details list)
            current_quantity = updated_inventory[item][0]
            # Calculate new quantity after order
            new_quantity = current_quantity - order_quantity
            
        # If new quantity is zero or less, mark as "Out of Stock"
        if new_quantity <= 0:
            updated_inventory[item][0] = "Out of Stock"
        else:
            updated_inventory[item][0] = new_quantity
    
    return updated_inventory