from .base import BiLateralMeasurement, SingleMeasurement
from .enums import archetypes, breath, association, right_left
from pydantic import BaseModel, Field


class ArmCare(BaseModel):
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


class MotorPreference(BaseModel):
    """Motor Preference assessment"""

    archetype: archetypes = Field(..., description="")
    extension_leg: right_left = Field(..., description="")
    breath_type: breath = Field(..., description="")
    association_type: association = Field(..., description="")


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


class HawkinsForcePlate(BaseModel):
    """Hawkins Force Plate Assessment"""

    cmj: SingleMeasurement = Field(..., description="")
    drop_jump: SingleMeasurement = Field(..., description="")
    pogo: SingleMeasurement = Field(..., description="")
    mid_thigh_pull: SingleMeasurement = Field(..., description="")
    mtp_time: SingleMeasurement = Field(..., description="")
    cop_ml: BiLateralMeasurement = Field(..., description="")
    cop_ap: BiLateralMeasurement = Field(..., description="")


class TrueStrength(BaseModel):
    """True Strength Assessment"""

    seated_shoulder_er: BiLateralMeasurement = Field(..., description="")
    seated_shoulder_ir: BiLateralMeasurement = Field(..., description="")
    shoulder_rotation: BiLateralMeasurement = Field(..., description="")
    shoulder_rotation_rfd: BiLateralMeasurement = Field(..., description="")
    hip_rotation: BiLateralMeasurement = Field(..., description="")
    hip_rotation_rfd: BiLateralMeasurement = Field(..., description="")
