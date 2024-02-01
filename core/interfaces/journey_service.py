from abc import ABC, abstractmethod

class JourneyService(ABC):
    @abstractmethod
    def add_boarding_card(self, card):
        pass

    @abstractmethod
    def get_journey(self):
        pass