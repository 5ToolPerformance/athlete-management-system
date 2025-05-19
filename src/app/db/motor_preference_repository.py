from typing import List, Optional
from uuid import UUID, uuid4
from src.app.models.assessments.motor_preference import (
    MotorPreferenceCreate,
    MotorPreferenceResponse,
)


class MotorPreferenceRepository:
    def __init__(self):
        self._repository: List[MotorPreferenceResponse] = []

    def create(self, data: MotorPreferenceCreate) -> MotorPreferenceResponse:
        assessment = MotorPreferenceResponse(id=uuid4(), **data.model_dump())
        self._repository.append(assessment)
        return assessment

    def get_by_id(self, id: UUID) -> Optional[MotorPreferenceResponse]:
        return next((a for a in self._repository if a.id == id), None)

    def list_all(self):
        return self._repository
