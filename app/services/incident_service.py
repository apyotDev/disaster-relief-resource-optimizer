from sqlalchemy.orm import Session,joinedload
from fastapi import HTTPException
from app.models.incident_model import Location,Incident,IncidentImpact,IncidentPrediction




# ==============================================
# GET REPORTS
#===============================================
def get_all_incidents(db: Session):
    # Eagerly load all child entities using standard SQL JOINs under the hood
    all_incidents = db.query(Incident).options(
        joinedload(Incident.location_metadata),
        joinedload(Incident.impact),
        joinedload(Incident.prediction)
    ).all()
    
    return all_incidents

#===============================================
# SAVING INCIDENT
#===============================================


def save_incident(
    db: Session,
    incident_data,
    prediction: dict
):

    
    location_record = Location(
            location=incident_data.location,
            latitude=incident_data.latitude,
            longitude=incident_data.longitude
        )
  
    # Initialize the core Incident record and bind the location metadata
    incident = Incident(
        disaster_type=incident_data.disaster_type,
        start_date=incident_data.start_date,
        end_date=incident_data.end_date,
        status=incident_data.status,
        description=incident_data.description,
        location_metadata=location_record  
    )

    # Instantiate and bind the standalone engineered metrics table row
    incident.impact = IncidentImpact(
        affected_rate=incident_data.affected_rate,
        damage_rate=incident_data.damage_rate,
        casualty_rate=incident_data.casualty_rate,
        homeless_rate=incident_data.homeless_rate,
        duration=incident_data.duration
    )

    # Instantiate and bind the ML/AI runtime prediction row
    incident.prediction = IncidentPrediction(
        relief_priority=prediction["relief_priority"],
        probability=prediction["probability"]
    )

    # Prsist the entire relational block to the database engine
    db.add(incident)
    db.commit()
    
    # Refreshing forces SQLAlchemy to pull the freshly minted foreign key attributes from PostgreSQL
    db.refresh(incident)

    return incident

# ====================================================
# INCIDENT STATUS UPDATE
# ====================================================




def update_incident_status(
    db: Session,
    incident_id: int,
    status: str
):
    # Use joinedload to fetch the core incident and all its related tables in a single SQL JOIN
    incident = db.query(Incident).options(
        joinedload(Incident.location_metadata),
        joinedload(Incident.impact),
        joinedload(Incident.prediction)
    ).filter(Incident.id == incident_id).first()

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found."
        )

    # Update the core table field
    incident.status = status

    db.commit()
    
    # Refreshing updates the fields while maintaining the eagerly loaded relations
    db.refresh(incident)

    return incident
