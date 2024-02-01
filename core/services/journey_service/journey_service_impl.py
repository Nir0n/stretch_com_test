from core.interfaces import JourneyService


class JourneyServiceImpl(JourneyService):
    def __init__(self):
        """
        Initialize the journey service with an empty list of boarding cards.
        """
        self.boarding_cards = []

    def add_boarding_card(self, card):
        """
        Add a boarding card to the journey.

        :param card: A boarding card.
        :type card: BoardingCard
        """
        self.boarding_cards.append(card)

    def __sort_boarding_cards(self):
        """
        Sort the boarding cards in the order of the journey, from departure to destination.
        """
        if not self.boarding_cards:
            return []

        departure_map = {card.departure: card for card in self.boarding_cards}
        destination_map = {card.destination: card for card in self.boarding_cards}

        start = None
        for departure in departure_map:
            if departure not in destination_map:
                start = departure
                break

        sorted_cards = []
        while start in departure_map:
            card = departure_map[start]
            sorted_cards.append(card)
            start = card.destination

        self.boarding_cards = sorted_cards

    def get_journey(self) -> str:
        """
        Get the sorted journey.
        :return: str
        """
        self.__sort_boarding_cards()
        journey_description = []
        for card in self.boarding_cards:
            description = f"Take {card.transport} from {card.departure} to {card.destination}. Sit in seat {card.seat}."
            journey_description.append(description)
        journey_description.append("You have arrived at your final destination.")
        return '\n'.join(journey_description)

