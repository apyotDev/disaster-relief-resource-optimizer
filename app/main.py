from fastapi import FastAPI
from app.services.predictor import DisasterPredictor
from app.routers.prediction import router


app = FastAPI(
    title="Disaster Relief Resource Optimizer API"
)


app.include_router(router)
app.state.predictor=DisasterPredictor()