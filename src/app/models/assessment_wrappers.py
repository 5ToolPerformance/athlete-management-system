from typing import Literal
from .assessments import ArmCare, MotorPreference, SMFA, HawkinsForcePlate, TrueStrength
from pydantic import BaseModel


class ArmCareWrapper(BaseModel):
    type: Literal["arm_care"]
    data: ArmCare


class MotorPreferenceWrapper(BaseModel):
    type: Literal["motor_preference"]
    data: MotorPreference


class SMFAWrapper(BaseModel):
    type: Literal["smfa"]
    data: SMFA


class HawkinsForcePlateWrapper(BaseModel):
    type: Literal["hawkins_force_plate"]
    data: HawkinsForcePlate


class TrueStrenthWrapper(BaseModel):
    type: Literal["true_strength"]
    data: TrueStrength
