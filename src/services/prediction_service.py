from src.core.logger import setup_logger
from src.ml.inference.predictor import Predictor
from src.ml.model_loader import ModelLoader
from src.core.config import config

logger = setup_logger(__name__)

class PredictionService:

    def __init__(self) -> None:
        self.model_loader = ModelLoader(model_path=config.model_path)
        self.predictor = Predictor()

    def predict(self, text: str) -> str:
        logger.info("Received prediction request")

        model = self.model_loader.get_model()

        logger.info("Using model: %s", model)

        prediction = self.predictor.predict(text)

        logger.info("Prediction result: %s", prediction)

        return prediction