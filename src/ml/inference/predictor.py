from src.core.constants import PredictionLabel

class Predictor:
    
    def predict(self, text: str) -> str:
        if len(text.strip()) == 0:
            return PredictionLabel.EMPTY
        
        if len(text) > 100:
            return PredictionLabel.LONG_TEXT
        
        return PredictionLabel.SHORT_TEXT