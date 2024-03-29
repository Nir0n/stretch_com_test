import unittest
from core.services.journey_service.journey_service_impl import JourneyServiceImpl as JourneyService # In tests we can use the implementation directly
from core.models.boarding_card import BoardingCard


class TestJourneyService(unittest.TestCase):

    def setUp(self):
        self.service = JourneyService()

        self.card1 = BoardingCard("Train 78A", "Madrid", "Barcelona", "45B")
        self.card2 = BoardingCard("Airport Bus", "Barcelona", "Gerona Airport",
                                  "No seat assignment")
        self.card3 = BoardingCard("Flight SK455", "Gerona Airport", "Stockholm", "3A")
        self.card4 = BoardingCard("Flight SK22", "Stockholm", "New York JFK", "7B")

    def test_add_boarding_card(self):
        # Test adding boarding cards
        self.service.add_boarding_card(self.card1)
        self.assertEqual(len(self.service.boarding_cards), 1)

    def test_sort_boarding_cards(self):
        # Test sorting boarding cards
        self.service.add_boarding_card(self.card3)
        self.service.add_boarding_card(self.card1)
        self.service.add_boarding_card(self.card4)
        self.service.add_boarding_card(self.card2)
        self.service._JourneyServiceImpl__sort_boarding_cards()

        self.assertEqual(self.service.boarding_cards[0].departure, "Madrid")
        self.assertEqual(self.service.boarding_cards[1].departure, "Barcelona")
        self.assertEqual(self.service.boarding_cards[2].departure, "Gerona Airport")
        self.assertEqual(self.service.boarding_cards[3].departure, "Stockholm")

    def test_get_journey(self):
        # Test the full journey description
        self.service.add_boarding_card(self.card1)
        self.service.add_boarding_card(self.card2)
        self.service.add_boarding_card(self.card3)
        self.service.add_boarding_card(self.card4)
        description = self.service.get_journey()

        self.assertIn("Take Train 78A from Madrid to Barcelona. Sit in seat 45B.", description)
        self.assertIn("You have arrived at your final destination.", description)