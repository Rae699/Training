"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify if Pac-Man can eat a ghost when empowered by a power pellet.

    :param power_pellet_active: bool - is the power pellet active?
    :param touching_ghost: bool - is Pac-Man touching a ghost?
    :return: bool - can ghost be eaten?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Check if Pac-Man has scored by eating a power pellet or dot.

    :param touching_power_pellet: bool - touching a power pellet?
    :param touching_dot: bool - touching a dot?
    :return: bool - has the player scored?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """End game when Pac-Man touches ghost without power pellet.

    :param power_pellet_active: bool - is power pellet active?
    :param touching_ghost: bool - is Pac-Man touching ghost?
    :return: bool - has player lost?
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger victory when all dots are eaten and ghosts are avoided.

    :param has_eaten_all_dots: bool - have all dots been eaten?
    :param power_pellet_active: bool - is power pellet active?
    :param touching_ghost: bool - is Pac-Man touching ghost?
    :return: bool - has player won?
    """
    return (has_eaten_all_dots 
            and not (not power_pellet_active and touching_ghost))
