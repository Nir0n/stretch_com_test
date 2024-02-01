from core.interfaces import JourneyService
from core.services.journey_service.journey_service_impl import JourneyServiceImpl


def get_journey_service() -> JourneyService:
    return JourneyServiceImpl()
