import argparse
import json
from dependency import get_journey_service
from core.models.boarding_card import BoardingCard


def main(boarding_cards):
    """
    Takes a list of boarding card information and prints the journey description.

    :param boarding_cards: A list of dictionaries, each representing a boarding card's information.
    :type boarding_cards: list of dict
    """
    service = get_journey_service()

    for card_info in boarding_cards:
        card = BoardingCard(**card_info)
        service.add_boarding_card(card)

    print(service.get_journey())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort and display a journey based on boarding cards")
    parser.add_argument('--boarding-cards', type=str, help='JSON list of boarding card data as strings')
    args = parser.parse_args()
    boarding_cards_arg = args.boarding_cards
    boarding_card_data = json.loads(boarding_cards_arg)
    main(boarding_card_data)