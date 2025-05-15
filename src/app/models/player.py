from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

from .assessments import MotorPreference
from .domains import StrengthAndConditioning
from .enums import Position, right_left


class Player(BaseModel):
    """Player class"""

    id: UUID = Field(default_factory=uuid4)
    first_name: str = Field(..., description="")
    last_name: str = Field(..., description="")
    dob: date = Field(..., description="")
    position: Position = Field(..., description="")
    height: float = Field(..., description="Player's height in inches")
    weight: float = Field(..., description="")
    hits: right_left = Field("Right", description="")
    throws: right_left = Field("Right", description="")
    motor_preference: MotorPreference = Field(..., description="")
    strength_and_conditioning: List[StrengthAndConditioning] = Field(
        default_factory=list
    )

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

    @property
    def latest_strength_assessment(self) -> Optional[StrengthAndConditioning]:
        if not self.strength_and_conditioning:
            return None
        return sorted(
            self.strength_and_conditioning, key=lambda x: x.created_on, reverse=True
        )[0]
