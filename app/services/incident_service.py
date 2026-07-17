from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.incident_model import Incident

#===============================================
# SAVING INCIDENT
#===============================================
def save_incident(
    db: Session,
    incident_data,
    prediction: dict
):
    incident = Incident(
        latitude=incident_data.latitude,
        longitude=incident_data.longitude,
        disaster_type=incident_data.disaster_type,
        affected_rate=incident_data.affected_rate,
        damage_rate=incident_data.damage_rate,
        casualty_rate=incident_data.casualty_rate,
        homeless_rate=incident_data.homeless_rate,
        duration=incident_data.duration,
        start_date=incident_data.start_date,
        end_date=incident_data.end_date,
        status=incident_data.status,
        description=incident_data.description,

        relief_priority=prediction["relief_priority"],
        probability=prediction["probability"]
    )

    db.add(incident)
    db.commit()
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

    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found."
        )

    incident.status = status

    db.commit()
    db.refresh(incident)

    return incident