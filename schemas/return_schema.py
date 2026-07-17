from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ReturnResponse(BaseModel,Generic[T]):
    status_code:int
    status:bool
    message:str
    data:Optional[T]=None
    