import pytest
from datetime import date
from pydantic import ValidationError
from src.app.models.domains import AthleticDevelopment
from src.app.models.assessments import ArmCare, SMFA, HawkinsForcePlate, TrueStrength
from src.app.models.base import SingleMeasurement, BiLateralMeasurement


@pytest.fixture
def valid_bilateral_measurement():
    return BiLateralMeasurement(right=10.0, left=9.0)


@pytest.fixture
def valid_single_measurement():
    return SingleMeasurement(value=10.0)


@pytest.fixture
def valid_arm_care(valid_bilateral_measurement):
    return ArmCare(
        shoulder_ir=valid_bilateral_measurement,
        shoulder_er=valid_bilateral_measurement,
        shoulder_flexion=valid_bilateral_measurement,
        supine_hip_er=valid_bilateral_measurement,
        supine_hip_ir=valid_bilateral_measurement,
        straight_leg_raise=valid_bilateral_measurement,
    )


@pytest.fixture
def valid_smfa(valid_bilateral_measurement, valid_single_measurement):
    return SMFA(
        pelvic_rotation=valid_bilateral_measurement,
        seated_trunk_rotation=valid_bilateral_measurement,
        ankle_test=valid_bilateral_measurement,
        forearm_test=valid_bilateral_measurement,
        cervical_rotation=valid_bilateral_measurement,
        msf=valid_bilateral_measurement,
        mse=valid_bilateral_measurement,
        msr=valid_bilateral_measurement,
        squat=valid_single_measurement,
        plevic_tilt_test=valid_single_measurement,
        cervical_flexion=valid_single_measurement,
        cervical_extension=valid_single_measurement,
    )


@pytest.fixture
def valid_hawkins(valid_bilateral_measurement, valid_single_measurement):
    return HawkinsForcePlate(
        cmj=valid_single_measurement,
        drop_jump=valid_single_measurement,
        pogo=valid_single_measurement,
        mid_thigh_pull=valid_single_measurement,
        mtp_time=valid_single_measurement,
        cop_ml=valid_bilateral_measurement,
        cop_ap=valid_bilateral_measurement,
    )


@pytest.fixture
def valid_true_strength(valid_bilateral_measurement):
    return TrueStrength(
        seated_shoulder_er=valid_bilateral_measurement,
        seated_shoulder_ir=valid_bilateral_measurement,
        shoulder_rotation=valid_bilateral_measurement,
        shoulder_rotation_rfd=valid_bilateral_measurement,
        hip_rotation=valid_bilateral_measurement,
        hip_rotation_rfd=valid_bilateral_measurement,
    )


class TestAthleticDevelopment:
    def test_valid_athletic_development(
        self, valid_arm_care, valid_smfa, valid_hawkins, valid_true_strength
    ):
        ad = AthleticDevelopment(
            created_on="2025-05-15",
            arm_care=valid_arm_care,
            smfa=valid_smfa,
            hawkins_assessment=valid_hawkins,
            true_strength=valid_true_strength,
        )
        assert ad.arm_care == valid_arm_care
        assert ad.smfa == valid_smfa
        assert ad.hawkins_assessment == valid_hawkins
        assert ad.true_strength == valid_true_strength
        assert ad.created_on == date(2025, 5, 15)
        assert ad.domain == "athletic_development"
