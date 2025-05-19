from pydantic import BaseModel, Field
from uuid import UUID


class CoachBase(BaseModel):
    first_name: str = Field(..., description="Coach's first name")
    last_name: str = Field(..., description="Coach's last name")

    class Config:
        orm_mode = True


class CoachCreate(CoachBase):
    pass


class CoachResponse(CoachBase):
    id: UUID
    full_name: str

    @property
    def full_name(self) -> str:
        """Returns the player's full name"""
        return f"{self.first_name} {self.last_name}"
