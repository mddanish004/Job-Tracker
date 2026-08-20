from enum import Enum

from pydantic import BaseModel



class User(BaseModel):
    name: str
    

class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    INTERVIEW = "INTERVIEW"
    OFFER = "OFFER"
    REJECTED = "REJECTED"


class JobApplicationCreate(BaseModel):
    company_name: str
    position: str
    status: ApplicationStatus
    job_url: str | None = None
    
    
class JobApplicationResponse(BaseModel):
    id: int
    company_name: str
    position: str
    status: ApplicationStatus
    job_url: str | None = None