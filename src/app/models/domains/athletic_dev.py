from pydantic import BaseModel
from uuid import UUID
from datetime import date


class AthleticDevelopmentBase(BaseModel):
    player_id: UUID
    coach_id: UUID
    arm_care: UUID
    smfa: UUID
    hawkins_assessment: UUID
    true_strength: UUID
    notes: str
    created_on: date

    class Config:
        orm_mode = True


class AthleticDevelopmentCreate(AthleticDevelopmentBase):
    pass


class AthleticDevelopmentResponse(AthleticDevelopmentBase):
    id: UUID
