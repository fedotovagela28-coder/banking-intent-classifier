from pydantic import BaseModel

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    intent: str
    confidence: float


class HealthResponse(BaseModel):
    status: str
    message: str