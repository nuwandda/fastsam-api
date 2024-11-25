from fastapi import APIRouter, HTTPException
from app.services.fastsam_service import FastSAMService
from app.api.schemas.fastsam import FastSAMRequest


router = APIRouter()
service = FastSAMService()

@router.post("/")
def process_fastsam(request: FastSAMRequest):
    try:
        result = service.process(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
