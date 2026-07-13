from pathlib import Path

import torch

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

from src.data.dataset_loader import get_label_names, load_banking77_dataset

MODEL_PATH = "artifacts/distilbert"
MAX_LENGTH = 128

dataset = load_banking77_dataset()
label_names = get_label_names(dataset)

class DistilBertService:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
        self.model.eval()

    def predict(self, text: str):
        inputs = self.tokenizer(
            text,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=-1)

        confidence_tensor, predicted_class_tensor = torch.max(
            probabilities,
            dim=-1,
        )

        predicted_class = predicted_class_tensor.item()
        confidence = confidence_tensor.item()

        return {
            "intent": label_names[predicted_class],
            "confidence": round(confidence, 4),
        }
