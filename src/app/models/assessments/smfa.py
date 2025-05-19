from uuid import UUID
from src.app.models.base import BiLateralMeasurement, SingleMeasurement
from pydantic import BaseModel, Field


class SMFA(BaseModel):
    """SMFA"""

    pelvic_rotation: BiLateralMeasurement = Field(..., description="")
    seated_trunk_rotation: BiLateralMeasurement = Field(..., description="")
    ankle_test: BiLateralMeasurement = Field(..., description="")
    forearm_test: BiLateralMeasurement = Field(..., description="")
    cervical_rotation: BiLateralMeasurement = Field(..., description="")
    msf: BiLateralMeasurement = Field(..., description="")
    mse: BiLateralMeasurement = Field(..., description="")
    msr: BiLateralMeasurement = Field(..., description="")
    squat: SingleMeasurement = Field(..., description="")
    plevic_tilt_test: SingleMeasurement = Field(..., description="")
    cervical_flexion: SingleMeasurement = Field(..., description="")
    cervical_extension: SingleMeasurement = Field(..., description="")

    class Config:
        orm_mode = True


class SMFACreate(SMFA):
    pass


class SMFAResponse(SMFA):
    id: UUID = Field(..., description="Unique identifyer for SMFA record")
