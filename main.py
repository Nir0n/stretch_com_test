from dependency import get_journey_service
from core.models.boarding_card import BoardingCard
def main(boarding_card_data):
    """
    Takes a list of boarding card information and prints the journey description.

    :param boarding_card_data: A list of dictionaries, each representing a boarding card's information.
    :type boarding_card_data: list of dict
    """
    service = get_journey_service()

    for card_info in boarding_card_data:
        card = BoardingCard(
            transport=card_info['transport'],
            departure=card_info['departure'],
            destination=card_info['destination'],
            seat=card_info['seat']
        )
        service.add_boarding_card(card)

    print(service.get_journey())


# Example usage:
if __name__ == "__main__":
    boarding_card_data = [
        {"transport": "Train 78A", "departure": "Madrid", "destination": "Barcelona",
         "seat": "45B"},
        {"transport": "Airport Bus", "departure": "Barcelona", "destination": "Gerona Airport",
         "seat": "No seat assignment"},
        {"transport": "Flight SK455", "departure": "Gerona Airport", "destination": "Stockholm",
         "seat": "3A", "extra_info": {"Gate": "45B", "Baggage drop": "ticket counter 344"}},
        {"transport": "Flight SK22", "departure": "Stockholm", "destination": "New York JFK",
         "seat": "7B", "extra_info": {"Gate": "22"}}
    ]

    main(boarding_card_data)