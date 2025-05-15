from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class SingleMeasurement(BaseModel):
    value: float = Field(..., description="Measurement value")


class BiLateralMeasurement(BaseModel):
    left: float = Field(..., description="Mesurement value for left side")
    right: float = Field(..., description="Measurement value for right side")

    @property
    def assymmetry(self) -> float:
        """Calculate asymmetry between left and right sides as percentage"""
        if self.left == 0 or self.right == 0:
            return 0.0
        max_value = max(self.left, self.right)
        min_value = min(self.left, self.right)
        return (1 - (min_value / max_value)) * 100


class Assessment(BaseModel):
    created_on: date = Field(..., description="Date that the assessment was performed")
    notes: Optional[str] = Field(None, description="Notes about the assessment")
