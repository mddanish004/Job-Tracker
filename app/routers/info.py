from fastapi import APIRouter

router= APIRouter()

@router.get("/info")
async def info():
    return {
    "name": "Job Application Tracker API",
    "version": "1.0.0",
    "status": "development"
}