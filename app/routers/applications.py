from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.database.session import get_session
from app.models.company import Company
from app.schemas.application import JobApplicationCreate, JobApplicationResponse



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
        
        
@router.post("/applications", response_model=JobApplicationResponse)
async def createApplication(job: JobApplicationCreate):
    return JobApplicationResponse(
        id= 1,
        company_name=job.company_name,
        position=job.position,
        status = job.status,
        job_url=job.job_url,
        
    )

@router.get("/test-db")
async def test_database(session: Session = Depends(get_session)):
    statement = select(Company)
    companies = session.exec(statement).all()
    
    return companies
    
    
