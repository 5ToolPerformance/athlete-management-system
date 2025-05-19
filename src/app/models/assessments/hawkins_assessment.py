from uuid import UUID
from src.app.models.base import BiLateralMeasurement, SingleMeasurement
from pydantic import BaseModel, Field


class HawkinsForcePlateBase(BaseModel):
    """Hawkins Force Plate Assessment"""

    cmj: SingleMeasurement = Field(..., description="")
    drop_jump: SingleMeasurement = Field(..., description="")
    pogo: SingleMeasurement = Field(..., description="")
    mid_thigh_pull: SingleMeasurement = Field(..., description="")
    mtp_time: SingleMeasurement = Field(..., description="")
    cop_ml: BiLateralMeasurement = Field(..., description="")
    cop_ap: BiLateralMeasurement = Field(..., description="")

    class Config:
        orm_mode = True


class HawkinsForcePlateCreate(HawkinsForcePlateBase):
    pass


class HawkinsForcePlateResponse(HawkinsForcePlateBase):
    id: UUID = Field(..., description="Unique identifyer for Hawkins Assessment entry")
