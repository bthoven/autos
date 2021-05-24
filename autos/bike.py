class Bike:

    def __init__(self, name: str):
        """Constructor.

        Args:
            name (str): Bike name.

        """
        self.name = name

    def ride(self, road: str) -> bool:
        """Ride.

        Args:
            road (str): Road to ride on.

        Returns:
            bool: True if successful.

        """
        print(f"Riding: {self.name} on road: {road}")
        return True
