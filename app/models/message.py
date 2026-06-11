from datetime import date
from pydantic import BaseModel


class Message(BaseModel):
    message_id: str
    date: date
    message_summary: str
