from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Text,
    DateTime,
    func,
)
from app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    # Location
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Disaster Information
    disaster_type = Column(String(50), nullable=False)

    # Engineered Features
    affected_rate = Column(Float, nullable=False)
    damage_rate = Column(Float, nullable=False)
    casualty_rate = Column(Float, nullable=False)
    homeless_rate = Column(Float, nullable=False)
    duration = Column(Integer, nullable=False)

    # Dates
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # Status
    status = Column(String(20), default="Active")

    # Description
    description = Column(Text)

    # Prediction
    relief_priority = Column(String)
    probability = Column(Float)

    # Audit Fields
    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )