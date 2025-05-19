from uuid import UUID
from src.app.models.assessments.arm_care import ArmCareCreate, ArmCareResponse
from src.app.db.arm_care_repository import ArmCareRepository
from typing import Optional, List


class ArmCareService:
    def __init__(self, repository: ArmCareRepository):
        self._repository = repository

    def create_assessment(self, data: ArmCareCreate) -> ArmCareResponse:
        return self._repository.create(data)

    def get_assessment(self, id: UUID) -> Optional[ArmCareResponse]:
        return self._repository.get_by_id(id)

    def list_assessment(self) -> List[ArmCareResponse]:
        return self._repository.list_all()
