from typing import List, Optional
from uuid import UUID, uuid4
from src.app.models.assessments.true_strength import (
    TrueStrengthCreate,
    TrueStrengthResponse,
)


class TrueStrengthRepository:
    def __init__(self):
        self._repository: List[TrueStrengthResponse] = []

    def create(self, data: TrueStrengthCreate) -> TrueStrengthResponse:
        assessment = TrueStrengthResponse(id=uuid4(), **data.model_dump())
        self._repository.append(assessment)
        return assessment

    def get_by_id(self, id: UUID) -> Optional[TrueStrengthResponse]:
        return next((a for a in self._repository if a.id == id), None)

    def list_all(self):
        return self._repository
