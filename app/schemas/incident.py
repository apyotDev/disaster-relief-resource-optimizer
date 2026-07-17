from pydantic import BaseModel
from datetime import datetime

class IncidentCreate(BaseModel):
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
    

class ClientResponse(IncidentCreate):
    id:int
    created_at:datetime
    updated_at:datetime

    class Config:
        from_attribute:True


class PredictionRequest(BaseModel):
    disaster_type: str
    affected_rate: float
    damage_rate: float
    casualty_rate: float
    homeless_rate: float
    duration: int

class StatusUpdate(BaseModel):
    status: str
