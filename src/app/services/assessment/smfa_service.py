from uuid import UUID
from src.app.models.assessments.smfa import SMFACreate, SMFAResponse
from src.app.db.smfa_repository import SMFARepository
from typing import Optional, List


class SMFAService:
    def __init__(self, repository: SMFARepository):
        self._repository = repository

    def create_assessment(self, data: SMFACreate) -> SMFAResponse:
        return self._repository.create(data)

    def get_assessment(self, id: UUID) -> Optional[SMFAResponse]:
        return self._repository.get_by_id(id)

    def list_assessment(self) -> List[SMFAResponse]:
        return self._repository.list_all()
