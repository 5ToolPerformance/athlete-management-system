from uuid import UUID
from src.app.models.base import BiLateralMeasurement
from pydantic import BaseModel, Field


class TrueStrengthBase(BaseModel):
    """True Strength Assessment"""

    seated_shoulder_er: BiLateralMeasurement = Field(..., description="")
    seated_shoulder_ir: BiLateralMeasurement = Field(..., description="")
    shoulder_rotation: BiLateralMeasurement = Field(..., description="")
    shoulder_rotation_rfd: BiLateralMeasurement = Field(..., description="")
    hip_rotation: BiLateralMeasurement = Field(..., description="")
    hip_rotation_rfd: BiLateralMeasurement = Field(..., description="")

    class Config:
        orm_mode = True


class TrueStrengthCreate(TrueStrengthBase):
    pass


class TrueStrengthResponse(TrueStrengthBase):
    id: UUID = Field(..., description="")
