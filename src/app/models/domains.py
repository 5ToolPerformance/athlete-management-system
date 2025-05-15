from typing import List, Optional
from pydantic import BaseModel, Field

from .base import Assessment
from .assessments import ArmCare, SMFA, HawkinsForcePlate, TrueStrength


class StrengthAndConditioning(Assessment):
    """Strength and Conditioning Assessment"""

    arm_care: List[ArmCare] = Field(default_factory=list)
    smfa: List[SMFA] = Field(default_factory=list)
    hawkins_force_plate: List[HawkinsForcePlate] = Field(default_factory=list)
    true_strength: List[TrueStrength] = Field(..., description="")
