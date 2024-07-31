from pydantic import BaseModel
from typing import Optional
class UserSchema(BaseModel):
    id : int
    name : Optional[str] = None
    nickname: Optional[str] = None
    email : Optional[str] = None
