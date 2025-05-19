from uuid import UUID
from src.app.models.assessments.true_strength import (
    TrueStrengthResponse,
    TrueStrengthCreate,
)
from src.app.db.true_strength_repository import TrueStrengthRepository
from typing import Optional, List


class ArmCareService:
    def __init__(self, repository: TrueStrengthRepository):
        self._repository = repository

    def create_assessment(self, data: TrueStrengthCreate) -> TrueStrengthResponse:
        return self._repository.create(data)

    def get_assessment(self, id: UUID) -> Optional[TrueStrengthResponse]:
        return self._repository.get_by_id(id)

    def list_assessment(self) -> List[TrueStrengthResponse]:
        return self._repository.list_all()
