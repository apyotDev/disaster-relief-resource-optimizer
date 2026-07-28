from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Location(Base):
    """Stores unique geographic metadata to prevent string replication."""
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    incidents = relationship("Incident", back_populates="location_metadata")


class Incident(Base):
    """The central hub connecting timing, disaster details, and operational data."""
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="RESTRICT"), nullable=False)
    
   
    disaster_type = Column(String(50), nullable=False)


    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)


    status = Column(String(20), default="Active")

   
    description = Column(Text)


    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)


    location_metadata = relationship("Location", back_populates="incidents")
    

    impact = relationship("IncidentImpact", back_populates="incident", uselist=False, cascade="all, delete-orphan")
    prediction = relationship("IncidentPrediction", back_populates="incident", uselist=False, cascade="all, delete-orphan")


class IncidentImpact(Base):
    """Isolates dynamic metrics and engineered analytic features."""
    __tablename__ = "incident_impacts"

   
    incident_id = Column(Integer, ForeignKey("incidents.id", ondelete="CASCADE"), primary_key=True)
    
    affected_rate = Column(Float, nullable=False)
    damage_rate = Column(Float, nullable=False)
    casualty_rate = Column(Float, nullable=False)
    homeless_rate = Column(Float, nullable=False)
    duration = Column(Integer, nullable=False)

   
    incident = relationship("Incident", back_populates="impact")


class IncidentPrediction(Base):
    """Separates volatile AI/ML inference records from structural schema rules."""
    __tablename__ = "incident_predictions"

    incident_id = Column(Integer, ForeignKey("incidents.id", ondelete="CASCADE"), primary_key=True)
    
    relief_priority = Column(String)
    probability = Column(Float)
    calculated_at = Column(DateTime, server_default=func.now(), nullable=False)

    incident = relationship("Incident", back_populates="prediction")
