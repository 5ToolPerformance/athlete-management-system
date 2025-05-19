from datetime import date
from pydantic import BaseModel, Field
from uuid import UUID

from .enums import Position, right_left


class PlayerBase(BaseModel):
    """Player class"""

    first_name: str = Field(..., description="")
    last_name: str = Field(..., description="")
    dob: date = Field(..., description="")
    position: Position = Field(..., description="")
    height: float = Field(..., description="Player's height in inches")
    weight: float = Field(..., description="")
    hits: right_left = Field("Right", description="")
    throws: right_left = Field("Right", description="")


class PlayerCreate(PlayerBase):
    pass


class PlayerResponse(PlayerBase):
    id: UUID
    full_name: str
    age: int

    @property
    def full_name(self) -> str:
        """Returns the player's full name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        """Get Player's age"""
        today = date.today()
        return (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )
