from typing import Any
from fastapi import Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class BaseResponse(BaseModel):
    data: Any
    message: str
    status: bool
    status_code: int
    
    def apply(self) -> Response:
        content = {
            "data": self.data,
            "message": self.message,
            "status": self.status,
            "status_code": self.status_code
        }
        return JSONResponse(content=content, status_code=self.status_code)