"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Initialize an Alien with coordinates and health.

        Args:
            x_coordinate: Initial x position
            y_coordinate: Initial y position
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Decrement the alien's health by 1."""
        self.health -= 1

    def is_alive(self) -> bool:
        """Check if the alien is alive.

        Returns:
            bool: True if health > 0, False otherwise
        """
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Update the alien's position to new coordinates.

        Args:
            new_x_coordinate: New x position to teleport to
            new_y_coordinate: New y position to teleport to
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        # To implement later once algo has been created and agreed on
        pass

    @classmethod
    def get_total_aliens_created(cls) -> int:
        """Get the total number of aliens created.

        Returns:
            int: Total number of aliens created so far
        """
        return cls.total_aliens_created
    
    
def new_aliens_collection(coordinates: list[tuple[int, int]]) -> list[Alien]:
    """Create a list of Alien instances from coordinate tuples.
    
    Args:
        coordinates: List of (x, y) coordinate tuples
        
    Returns:
        list[Alien]: List of Alien instances at the specified coordinates
    """
    # Step 1: Create an empty list to store our Alien instances
    alien_list = []
    
    # Step 2: Iterate through each coordinate tuple
    for x, y in coordinates:
        # Step 3: Create a new Alien instance with the coordinates
        new_alien = Alien(x, y)
        
        # Step 4: Add the new alien to our list
        alien_list.append(new_alien)
    
    # Step 5: Return the complete list of aliens
    return alien_list
    
        
    
