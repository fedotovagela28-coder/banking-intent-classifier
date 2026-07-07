from fastapi import Request
from fastapi.responses import JSONResponse

from src.core.exceptions import AppError

async def app_error_handler(request: Request, error: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"status": "error",
                 "message": str(error),
                 },
    )