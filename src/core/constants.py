from enum import StrEnum

class PredictionLabel(StrEnum):
    EMPTY = "empty"
    SHORT_TEXT = "short_text"
    LONG_TEXT ="long_text"

class ServiceStatus(StrEnum):
    OK = "ok"
    ERROR = "error"