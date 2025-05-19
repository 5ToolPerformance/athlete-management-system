from uuid import UUID
from src.app.models.enums import archetypes, breath, association, right_left
from pydantic import BaseModel, Field


class MotorPreferenceBase(BaseModel):
    """Motor Preference assessment"""

    archetype: archetypes = Field(..., description="")
    extension_leg: right_left = Field(..., description="")
    breath_type: breath = Field(..., description="")
    association_type: association = Field(..., description="")

    class Config:
        orm_mode = True


class MotorPreferenceCreate(MotorPreferenceBase):
    pass


class MotorPreferenceResponse(MotorPreferenceBase):
    id: UUID = Field(..., description="")
