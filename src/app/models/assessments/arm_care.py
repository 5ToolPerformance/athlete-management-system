from uuid import UUID
from src.app.models.base import BiLateralMeasurement
from pydantic import BaseModel, Field


class ArmCareBase(BaseModel):
    """ArmCare assessment"""

    shoulder_ir: BiLateralMeasurement = Field(
        ..., description="Shoulder IR measurement"
    )
    shoulder_er: BiLateralMeasurement = Field(
        ..., description="Shoulder ER measurement"
    )
    shoulder_flexion: BiLateralMeasurement = Field(
        ..., description="Shoulder Flexion measurement"
    )
    supine_hip_ir: BiLateralMeasurement = Field(
        ..., description="Supine Hip IR measurement"
    )
    supine_hip_er: BiLateralMeasurement = Field(
        ..., description="Supine Hip ER measurement"
    )
    straight_leg_raise: BiLateralMeasurement = Field(
        ..., description="Straight Leg Raise measurement"
    )

    class Config:
        orm_mode = True


class ArmCareCreate(ArmCareBase):
    pass


class ArmCareResponse(ArmCareBase):
    id: UUID
