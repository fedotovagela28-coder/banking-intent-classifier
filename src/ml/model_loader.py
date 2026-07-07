from src.core.exceptions import ModelLoadError, ModelNotLoadedError
from src.core.logger import setup_logger

logger = setup_logger(__name__)

class ModelLoader:
    "loads .pkl models, pytorch .pt models, huggingface models, onnx models ..."

    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = model_path
        self.model = None

    def load(self) -> None:
        try:
            logger.info("Loading model from path: %s", self.model_path)

            #Placeholder for real model loading logic.
            self.model = "dummy_model"

            logger.info("Model loaded successfully")
        
        except Exception as error:
            logger.exception("Model loading failed")
            raise ModelLoadError("Failed to load model") from error

    def get_model(self) -> str:
        if self.model is None:
            self.load()

        return self.model