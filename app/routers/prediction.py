from fastapi import APIRouter, Request,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.incident import IncidentCreate,StatusUpdate
from app.database import get_db
from app.services.incident_service import  save_incident, update_incident_status,get_all_incidents

router = APIRouter(
    prefix="/disaster-relief-optimize-api",
    tags=["Prediction"]
)

# ==============================================
# HOME
# ==============================================
@router.get("/",status_code=status.HTTP_200_OK)
def home():
    return{"message":"Welcome to Disaster Relief API"}
# ==============================================
# GETTING REPORTS 
# ==============================================
@router.get("/incidents",status_code=status.HTTP_200_OK)
def _get_all_incidents(db:Session=Depends(get_db)):

    print(get_all_incidents(db))
    try:
        all_incidents=get_all_incidents(db)
        print(all_incidents)
    except Exception as e:
        
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    return all_incidents



# ==============================================
# PREDICTION FOR INCIDENT
# ==============================================


@router.post("/predict",status_code=status.HTTP_201_CREATED)
def predict(
    request: Request,
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):

    predictor = request.app.state.predictor
    result = predictor.predict(incident.model_dump())

    try:
        saved_incident = save_incident(
            db,
            incident,
            result
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    return {"status": "success","status_code": status.HTTP_201_CREATED,""
                "message": "Incident predicted and saved successfully.",
                "data": {
                    "incident_id": saved_incident.id, "prediction": {
                    "relief_priority": saved_incident.prediction.relief_priority,
                    "probability": round(saved_incident.prediction.probability, 6)},
                "incident": {
                    "latitude": incident.latitude,
                    "longitude":incident.longitude,
                    "disaster_type": incident.disaster_type.title(),
                    "status": saved_incident.status,
                    "created_at": saved_incident.created_at}
                    }
                }



# ========================================================
# UPDATING INCIDENT STATUS
# ========================================================


@router.put("/{incident_id}/status",status_code=status.HTTP_200_OK)
def update_status(
    incident_id: int,
    update: StatusUpdate,
    db: Session = Depends(get_db)
):

    incident = update_incident_status(
        db,
        incident_id,
        update.status
    )

    return {
        "status": "success",
        "status_code": 200,
        "message": "Incident status updated successfully.",
        "data": {
            "incident_id": incident.id,
            "status": incident.status,
            "updated_at": incident.updated_at
        }
    }
