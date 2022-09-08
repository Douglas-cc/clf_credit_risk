from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List


class InputData(BaseModel):
    id: Optional[int] = None
    name: str
    income: float
    age: float 
    loan: float
    date: datetime = Field(default_factory=datetime.now) 
        
    class Config:
        orm_mode = True  
