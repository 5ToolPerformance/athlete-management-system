from uuid import UUID
from src.app.models.assessments.hawkins_assessment import (
    HawkinsForcePlateCreate,
    HawkinsForcePlateResponse,
)
from src.app.db.hawkins_repository import HawkinsForcePlateRepository
from typing import Optional, List


class HawkinsForcePlateService:
    def __init__(self, repository: HawkinsForcePlateRepository):
        self._repository = repository

    def create_assessment(
        self, data: HawkinsForcePlateCreate
    ) -> HawkinsForcePlateResponse:
        return self._repository.create(data)

    def get_assessment(self, id: UUID) -> Optional[HawkinsForcePlateResponse]:
        return self._repository.get_by_id(id)

    def list_assessment(self) -> List[HawkinsForcePlateResponse]:
        return self._repository.list_all()
