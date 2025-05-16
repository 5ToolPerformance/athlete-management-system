from typing import List, Union, Literal
from pydantic import Field
from datetime import date

from .base import BaseLesson
from .assessments import ArmCare, SMFA, HawkinsForcePlate, TrueStrength


class AthleticDevelopment(BaseLesson):
    """Strength and Conditioning Assessment"""

    domain: Literal["athletic_development"] = Field(
        "athletic_development", description=""
    )
    created_on: date = Field(..., description="Date of lesson")
    arm_care: ArmCare = Field(..., description="")
    smfa: SMFA = Field(..., description="")
    hawkins_assessment: HawkinsForcePlate = Field(..., description="")
    true_strength: TrueStrength = Field(..., description="")

    @property
    def mpr_l(self):
        # V_Power
        v_pow = (
            self.hawkins_assessment.mid_thigh_pull
            + self.hawkins_assessment.cmj
            + self.hawkins_assessment.drop_jump
            + self.hawkins_assessment.pogo
        ) / 4
        n_v_pow = (v_pow - 0.1) / (2000 - 0.1)

        # Total Rotation
        t_rot = (
            (
                self.true_strength.shoulder_rotation.left
                + self.true_strength.shoulder_rotation_rfd.left
            )
            + (
                self.true_strength.hip_rotation.left
                + self.true_strength.hip_rotation_rfd.left
            )
        ) / 4
        n_t_rot = (t_rot - 0.1) / (40000 - 0.1)

        # Arm Strength
        arm_strength = (
            self.true_strength.seated_shoulder_er.left
            + self.true_strength.seated_shoulder_ir.left
        ) / 2

        power_rating = (n_v_pow * 0.3) + (n_t_rot * 0.4) + (arm_strength * 0.3)
        return power_rating


LessonType = List[Union[AthleticDevelopment]]
