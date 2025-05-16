import pytest
from datetime import date
from pydantic import ValidationError
from src.app.models.base import (
    BiLateralMeasurement,
    SingleMeasurement,
    BaseAssessment,
    BaseLesson,
)


class TestBaseMeasurements:
    def test_bilateral_measurement_valid(self):
        """Test for valid bilateral measurement"""

        measurement = BiLateralMeasurement(left=10.0, right=9.0)
        assert measurement.left == 10.0
        assert measurement.right == 9.0

    def test_bilateral_measurement_invalid(self):
        """Test for invalid bilateral measurement"""

        with pytest.raises(ValidationError):
            BiLateralMeasurement(left="Invalid", right=13.0)

        with pytest.raises(ValidationError):
            BiLateralMeasurement(left=10.0, right="Invalid")

    def test_singular_measurement_valid(self):
        """Test for valud singular measurement"""

        measurement = SingleMeasurement(value=30.9)
        assert measurement.value == 30.9

    def test_singular_measurment_invalid(self):
        """Test for invalid singular measurement"""

        with pytest.raises(ValidationError):
            SingleMeasurement(value="Invalid")


class TestAssessment:
    def test_assessment_valid(self):
        """Test for a valid assessment"""

        assessment = BaseAssessment(type="test", notes="These are notes")
        assert assessment.notes == "These are notes"
        assert assessment.type == "test"

    def test_assessment_string_valid(self):
        """Test for a valid string date"""

        assessment = BaseAssessment(type="test")
        assert assessment.type == "test"

    def test_assessment_invalid(self):
        """Test for invalid assessment"""

        with pytest.raises(ValidationError):
            BaseAssessment(created_on=100, notes="Notes")
        with pytest.raises(ValidationError):
            BaseAssessment(created_on=date.today, notes=1000)

    def test_lesson_valid(self):
        """Test for valid Base lesson"""

        d = "2025-05-15"
        lesson = BaseLesson(domain="test", created_on=d)
        assert lesson.domain == "test"
        assert lesson.created_on == date(2025, 5, 15)
