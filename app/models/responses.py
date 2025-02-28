"""Standard API response models"""

from typing import Any, Optional
from pydantic import BaseModel


class StandardResponse(BaseModel):
    """Standard API response format"""

    success: bool
    message: str
    data: Optional[Any] = None
