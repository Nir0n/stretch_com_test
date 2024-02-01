class BoardingCard:
    def __init__(self, transport, departure, destination, seat):
        """
        Initialize a boarding card.

        :param transport: Means of transportation (e.g., 'Train 78A', 'Flight SK455').
        :type transport: str
        :param departure: Departure location.
        :type departure: str
        :param destination: Destination location.
        :type destination: str
        :param seat: Seat assignment (e.g., '45B', 'No seat assignment').
        :type seat: str
        """
        self.transport = transport
        self.departure = departure
        self.destination = destination
        self.seat = seat
