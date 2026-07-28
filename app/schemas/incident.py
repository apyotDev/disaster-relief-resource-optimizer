from pydantic import BaseModel, computed_field
from datetime import datetime

class IncidentCreate(BaseModel):
    location: str
    latitude: float
    longitude: float
    disaster_type: str
    affected_rate: float
    damage_rate: float
    casualty_rate: float
    homeless_rate: float
    duration: int
    start_date: datetime
    end_date: datetime | None = None
    status: str = "Active"
    description: str | None = None


class ClientResponse(BaseModel):
    id: int
    disaster_type: str
    start_date: datetime
    end_date: datetime | None = None
    status: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime


    #FLATTENING LOCATIONS DATA
    @computed_field
    def location(self) -> str:
        return self.location_metadata.location if self.location_metadata else ""

    @computed_field
    def latitude(self) -> float:
        return self.location_metadata.latitude if self.location_metadata else 0.0

    @computed_field
    def longitude(self) -> float:
        return self.location_metadata.longitude if self.location_metadata else 0.0

    # FLATTENING IMPACT METRICS
    @computed_field
    def affected_rate(self) -> float:
        return self.impact.affected_rate if self.impact else 0.0

    @computed_field
    def damage_rate(self) -> float:
        return self.impact.damage_rate if self.impact else 0.0

    @computed_field
    def casualty_rate(self) -> float:
        return self.impact.casualty_rate if self.impact else 0.0

    @computed_field
    def homeless_rate(self) -> float:
        return self.impact.homeless_rate if self.impact else 0.0

    @computed_field
    def duration(self) -> int:
        return self.impact.duration if self.impact else 0

    # FLATTENING PREDICTION METRICS
    @computed_field
    def relief_priority(self) -> str | None:
        return self.prediction.relief_priority if self.prediction else None

    @computed_field
    def probability(self) -> float | None:
        return self.prediction.probability if self.prediction else None

    
    model_config = {
        "from_attributes": True
    }


class PredictionRequest(BaseModel):
    disaster_type: str
    affected_rate: float
    damage_rate: float
    casualty_rate: float
    homeless_rate: float
    duration: int


class StatusUpdate(BaseModel):
    status: str
