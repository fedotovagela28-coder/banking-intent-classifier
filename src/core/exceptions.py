class AppError(Exception):
    """Base class for all application errors."""

class ConfigurationError(AppError):
    """Raised when application configuration in invalid."""

class ModelLoadError(AppError):
    """Raised when model loading fails."""

class ModelNotLoadedError(AppError):
    """Raised when model is requested before loading."""

class PredictionError(AppError):
    """Raised when prediction fails."""