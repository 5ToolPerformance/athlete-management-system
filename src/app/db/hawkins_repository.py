from typing import List, Optional
from uuid import UUID, uuid4
from src.app.models.assessments.hawkins_assessment import (
    HawkinsForcePlateCreate,
    HawkinsForcePlateResponse,
)


class HawkinsForcePlateRepository:
    def __init__(self):
        self._repository: List[HawkinsForcePlateResponse] = []

    def create(self, data: HawkinsForcePlateCreate) -> HawkinsForcePlateResponse:
        assessment = HawkinsForcePlateResponse(id=uuid4(), **data.model_dump())
        self._repository.append(assessment)
        return assessment

    def get_by_id(self, id: UUID) -> Optional[HawkinsForcePlateResponse]:
        return next((a for a in self._repository if a.id == id), None)

    def list_all(self):
        return self._repository
