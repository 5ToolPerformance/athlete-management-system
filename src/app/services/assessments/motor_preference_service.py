from uuid import UUID
from src.app.models.assessments.motor_preference import (
    MotorPreferenceResponse,
    MotorPreferenceCreate,
)
from src.app.db.motor_preference_repository import MotorPreferenceRepository
from typing import Optional, List


class MotorPreferenceService:
    def __init__(self, repository: MotorPreferenceRepository):
        self._repository = repository

    def create_assessment(self, data: MotorPreferenceCreate) -> MotorPreferenceResponse:
        return self._repository.create(data)

    def get_assessment(self, id: UUID) -> Optional[MotorPreferenceResponse]:
        return self._repository.get_by_id(id)

    def list_assessment(self) -> List[MotorPreferenceResponse]:
        return self._repository.list_all()
