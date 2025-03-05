from Exercism.python.inventory-management.dicts import add_items

"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    
# The MVP should allow the user to add items to their shopping cart. This could be a single item or multiple items at once. 
# Since this is an MVP, item quantity is indicated by repeats. If a user wants to add 2 Oranges, 'Oranges' will appear twice in the input iterable. 
# If the user already has the item in their cart, the cart quantity should be increased by 1. 
# If the item is new to the cart, it should be added with a quantity of 1.
# Create the function add_item(<current_cart>, <items_to_add>) that takes a cart dictionary and any list-like iterable of items to add as arguments. 
# It should return a new/updated shopping cart dictionary for the user.
# >>> add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
#               ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))
# {'Banana': 4, 'Apple': 5, 'Orange': 2}
# >>> add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
#               ['Banana', 'Orange', 'Blueberries', 'Banana'])
# {'Banana': 5, 'Apple': 2, 'Orange': 2, 'Blueberries': 1}

    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart



def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

# paUh-oh. Looks like the product team is engaging in feature creep. They want to add extra functionality to the MVP. 
# The application now has to create a shopping cart by reading items off a users notes app. 
# Convenient for the users, but slightly more work for the team.
# Create the function read_notes(<notes>) that can take any list-like iterable as an argument. 
# The function should parse the items and create a user shopping cart/dictionary. 
# Each item should be added with a quantity of 1. The new user cart should then be returned.

# >>> read_notes(('Banana','Apple', 'Orange'))
# {'Banana': 1, 'Apple': 1, 'Orange': 1}

# >>> read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple'])
# {'Blueberries' : 1, 'Pear' : 1, 'Orange' : 1, 'Banana' : 1, 'Apple' : 1}

    shopping_cart = {}
    for item in notes:
        shopping_cart[item] = 1
    return shopping_cart
        


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

# The app has an "ideas" section that's filled with finished recipes from various cuisines. The user can select any one of these recipes and have 
# all its ingredients added to their shopping cart automatically. The project manager has asked you create a way to edit these "ideas" recipes, 
# since the content team keeps changing around ingredients and quantities.

# Create the function update_recipes(<ideas>, <recipe_updates>) that takes an "ideas" dictionary and an iterable of recipe updates as arguments. 
# The function should return the new/updated "ideas" dictionary.

# >>> update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
# (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
# ...
# {'Banana Bread' : {'Banana': 4,  'Apple': 1, 'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3},
#  'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
# >>> update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
#                     'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
# [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
# ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
# ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})])
# ...
# {'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#  'Raspberry Pie': {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2},
#  'Pasta Primavera': {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1},
#  'Blueberry Crumble': {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3}}

    for recipe_name, ingredients in recipe_updates:
        ideas[recipe_name] = ingredients
    return ideas 


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    # Needs a dictionary
    # Goal: Copy it (no reference, real copy), sort it
    # How? Get the items using dict.items, sort them using sorted(), return a dict to ensure
    
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # Create empty fulfillment cart
    fulfillment_cart = {}
    
    # For each item in the cart
    for item, quantity in cart.items():
        # Get the aisle info (a list containing [aisle_number, needs_refrigeration])
        aisle_info = aisle_mapping[item]
        # Create new list with [quantity, aisle_number, needs_refrigeration]
        fulfillment_cart[item] = [quantity, aisle_info[0], aisle_info[1]]
    
    # Return a new dict sorted by keys in reverse order
    return dict(sorted(fulfillment_cart.items(), reverse=True))
    
    


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.""" 
    
    # APPROACH 1: Classical Procedural Way 
    
    # Step 1: Make a copy of store inventory to modify
    updated_inventory = store_inventory.copy() 
    
    # Step 2: Loop through each item in fulfillment cart
    for item, details in fulfillment_cart.items(): 
        # Get ordered quantity from fulfillment cart
        ordered_quantity = details[0] 
        
        # Get current store quantity
        current_store_quantity = store_inventory[item][0]
        
        # Calculate new quantity
        new_quantity = current_store_quantity - ordered_quantity
        
        # Check if out of stock
        if new_quantity <= 0:
            # Keep aisle and refrigeration info, just change quantity to "Out of Stock"
            updated_inventory[item][0] = "Out of Stock"
        else:
            # Update with new quantity
            updated_inventory[item][0] = new_quantity
            
    return updated_inventory

    # APPROACH 2: Pythonic Way
    # return {
    #     item: ["Out of Stock" if store_inventory[item][0] - order_details[0] <= 0 
    #         else store_inventory[item][0] - order_details[0], 
    #           *store_inventory[item][1:]]
    #     for item, order_details in fulfillment_cart.items()
    # }