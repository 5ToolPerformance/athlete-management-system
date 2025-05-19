from typing import List, Optional
from uuid import UUID, uuid4
from src.app.models.assessments.smfa import SMFACreate, SMFAResponse


class SMFARepository:
    def __init__(self):
        self._repository: List[SMFAResponse] = []

    def create(self, data: SMFACreate) -> SMFAResponse:
        assessment = SMFAResponse(id=uuid4(), **data.model_dump())
        self._repository.append(assessment)
        return assessment

    def get_by_id(self, id: UUID) -> Optional[SMFAResponse]:
        return next((a for a in self._repository if a.id == id), None)

    def list_all(self):
        return self._repository
