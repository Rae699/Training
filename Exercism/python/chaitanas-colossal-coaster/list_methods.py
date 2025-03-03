"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    # Define the add_me_to_the_queue() function that takes 4 parameters <express_queue>, <normal_queue>, <ticket_type>, 
    # <person_name> and returns the appropriate queue updated with the person's name.
    # <ticket_type> is an int with 1 == express_queue and 0 == normal_queue.
    # <person_name> is the name (as a str) of the person to be added to the respective queue.
    # >>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], 
    # ticket_type=1, person_name="RichieRich")
    # ...
    # ["Tony", "Bruce", "RichieRich"]
    # >>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], 
    # ticket_type=0, person_name="HawkEye")
    # ....
    # ["RobotGuy", "WW", "HawkEye"]

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    

def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

# One person arrived late at the park but wants to join the queue where their friends are waiting. 
# But they have no idea where their friends are standing and there isn't any phone reception to call them.
# Define the find_my_friend() function that takes 2 parameters queue and friend_name and returns the position in the queue of the person's name.
# <queue> is the list of people standing in the queue.
# <friend_name> is the name of the friend whose index (place in the queue) you need to find.
# Remember: Indexing starts at 0 from the left, and -1 from the right.

# >>> find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve")
# ...
# 1

    return queue.index(friend_name) #This is not an in place modification of a list so it wont return None but the actual value of what we looking for!


def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    # Now that their friends have been found (in task #2 above), the late arriver would like to join them at their place in the queue. 
    # Define the add_me_with_my_friends() function that takes 3 parameters queue, index, and person_name.
    # <queue> is the list of people standing in the queue.
    # <index> is the position at which the new person should be added.
    # <person_name> is the name of the person to add at the index position.
    # Return the queue updated with the late arrivals name.
    # >>> add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky")
    # ...
    # ["Natasha", "Bucky", "Steve", "T'challa", "Wanda", "Rocket"]

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    # You just heard from the queue that there is a really mean person shoving, shouting, and making trouble. You need to throw that miscreant out for bad behavior!
    # Define the remove_the_mean_person() function that takes 2 parameters queue and person_name.
    # <queue> is the list of people standing in the queue.
    # <person_name> is the name of the person that needs to be kicked out.
    # Return the queue updated without the mean person's name.
    # >>> remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
    # ["Natasha", "Steve", "Wanda", "Rocket"]

    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

# You may not have seen two unrelated people who look exactly the same, but you have definitely seen unrelated people with the exact same name (namefellows)!
# Today, it looks like there are a lot of them in attendance. You want to know how many times a particular name occurs in the queue.
# Define the how_many_namefellows() function that takes 2 parameters queue and person_name.
# <queue> is the list of people standing in the queue.
# <person_name> is the name you think might occur more than once in the queue.
# Return the number of occurrences of person_name, as an int.
# >>> how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
# 2

    return queue.count(person_name)


def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

# Sadly, it's overcrowded at the park today and you need to remove the last person in the normal line (you will give them a voucher to come back in the fast-track on another day).
# You will have to define the function remove_the_last_person() that takes 1 parameter queue, which is the list of people standing in the queue.
# You should update the list and also return the name of the person who was removed, so you can write them a voucher.
# >>> remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
# ...
# 'Rocket'

    return queue.pop()


def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    original = queue.copy()
    return sorted(queue)
