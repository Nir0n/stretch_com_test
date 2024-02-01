from abc import ABC, abstractmethod

class JourneyService(ABC):
    @abstractmethod
    def add_boarding_card(self, card):
        pass

    @abstractmethod
    def sort_boarding_cards(self):
        pass