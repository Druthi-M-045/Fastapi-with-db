from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HistoryBase(BaseModel):
    input_text: str
    output_text: str

class HistoryCreate(HistoryBase):
    pass

class HistoryResponse(HistoryBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True
