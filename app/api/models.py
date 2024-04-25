from pydantic import BaseModel
from typing import List, Optional


class BilliardIn(BaseModel):
    name: str
    description: str
    address: str
    country: str
    club_id: List[int]


class BilliardOut(BilliardIn):
    id: int


class ArtistUpdate(BilliardIn):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None
    billiard_id: Optional[List[int]] = None