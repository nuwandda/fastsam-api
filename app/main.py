from fastapi import FastAPI
from app.config import Config
from app.api.endpoints import fastsam


app = FastAPI()

# Include FastSAM routes
app.include_router(fastsam.router, prefix="/fastsam", tags=["FastSAM"])

@app.get("/")
def read_root():
    return {"status": "FastSAM API is running"}
