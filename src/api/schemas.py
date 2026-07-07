from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=1)

class PredictionResponse(BaseModel):
    prediction: str

class HealthResponse(BaseModel):
    status: str
    message: str