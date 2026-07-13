from fastapi import FastAPI

from src.api.schemas import HealthResponse, PredictionRequest, PredictionResponse
from src.core.config import config
from src.services.prediction_service import PredictionService
from src.core.constants import ServiceStatus
from src.api.exception_handlers import app_error_handler
from src.core.exceptions import AppError

app = FastAPI(
    title=config.app_name,
    description="Simple FastAPI service for ML inference.",
    version=config.app_version,
)
app.add_exception_handler(AppError, app_error_handler)

prediction_service = PredictionService()

@app.get("/", response_model=HealthResponse)
def root() -> HealthResponse:
    return HealthResponse(status=ServiceStatus.OK, message="ML API is running")

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status=ServiceStatus.OK, message="Service is healthy")

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    prediction = prediction_service.predict(request.text)
    return PredictionResponse(intent=prediction["intent"], confidence=prediction["confidence"])