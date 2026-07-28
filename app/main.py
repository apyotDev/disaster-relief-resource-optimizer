from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.predictor import DisasterPredictor
from app.routers.prediction import router


app = FastAPI(
    title="Disaster Relief Resource Optimizer API"
)

app.add_middleware(
    CORSMiddleware,allow_origins=[
        "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://Disaster-relief-optimizer.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router)
app.state.predictor=DisasterPredictor()