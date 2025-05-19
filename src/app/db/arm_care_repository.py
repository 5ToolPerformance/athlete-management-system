from typing import List, Optional
from uuid import UUID, uuid4
from src.app.models.assessments.arm_care import ArmCareCreate, ArmCareResponse


class ArmCareRepository:
    def __init__(self):
        self._repository: List[ArmCareResponse] = []

    def create(self, data: ArmCareCreate) -> ArmCareResponse:
        assessment = ArmCareResponse(id=uuid4(), **data.model_dump())
        self._repository.append(assessment)
        return assessment

    def get_by_id(self, id: UUID) -> Optional[ArmCareResponse]:
        return next((a for a in self._repository if a.id == id), None)

    def list_all(self):
        return self._repository
