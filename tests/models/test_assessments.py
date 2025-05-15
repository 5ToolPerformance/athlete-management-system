import pytest
from pydantic import ValidationError
from src.app.models.assessments import (
    ArmCare,
    SMFA,
    MotorPreference,
    HawkinsForcePlate,
    TrueStrength,
)
from src.app.models.base import BiLateralMeasurement, SingleMeasurement


@pytest.fixture
def valid_bilateral_measurement():
    return BiLateralMeasurement(right=10.0, left=9.0)


@pytest.fixture
def valid_single_measurement():
    return SingleMeasurement(value=10.0)


class TestArmCare:
    def test_armcare(self, valid_bilateral_measurement):
        """Test constructor for armcare"""

        arm_care = ArmCare(
            shoulder_ir=valid_bilateral_measurement,
            shoulder_er=valid_bilateral_measurement,
            shoulder_flexion=valid_bilateral_measurement,
            supine_hip_er=valid_bilateral_measurement,
            supine_hip_ir=valid_bilateral_measurement,
            straight_leg_raise=valid_bilateral_measurement,
        )

        assert arm_care.shoulder_er.right == 10.0
        assert arm_care.shoulder_er.left == 9.0
        assert arm_care.shoulder_ir.right == 10.0
        assert arm_care.shoulder_ir.left == 9.0
        assert arm_care.shoulder_flexion.right == 10.0
        assert arm_care.shoulder_flexion.left == 9.0
        assert arm_care.supine_hip_er.right == 10.0
        assert arm_care.supine_hip_er.left == 9.0
        assert arm_care.supine_hip_ir.right == 10.0
        assert arm_care.supine_hip_ir.left == 9.0
        assert arm_care.straight_leg_raise.right == 10.0
        assert arm_care.straight_leg_raise.left == 9.0
