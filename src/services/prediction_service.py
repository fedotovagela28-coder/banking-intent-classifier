from src.core.logger import setup_logger
from src.services.distilbert_service import DistilBertService
from src.core.config import config

logger = setup_logger(__name__)

class PredictionService:

    def __init__(self) -> None:
        self.distilbert = DistilBertService()

    def predict(self, text: str) -> str:
        logger.info("Received prediction request")

        prediction = self.distilbert.predict(text)

        logger.info("Prediction result: %s", prediction)

        return prediction