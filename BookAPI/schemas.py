# Schemas for JSON responses

from typing import List, Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    Title: str
    Content: str


class Book(BookBase):
    ID: int
    Value: int
    Author: str
    Description: str
    Type: str

    class Config:
        orm_mode = True