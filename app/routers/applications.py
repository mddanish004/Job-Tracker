from fastapi import APIRouter

router = APIRouter()

@router.get("/applications/{application_id}")
async def get_application(application_id: int):
    return {
        "application_id": application_id,
        "message": "Application retrieved successfully"
    }

@router.get("/applications")
async def get_application_by_status(status: str | None=None):
    if status:
        return {
            "status": status,
            "message": "Applications retrieved successfully"
        }
    else:
        return {
            "status": None,
            "message": "Applications retrieved successfully"
        }