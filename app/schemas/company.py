from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    website: str | None = None
    
class CompanyResponse(BaseModel):
    id: int
    name:str
    website: str | None = None
    
class CompanyUpdate(BaseModel):
    name: str | None = None
    website: str | None = None
    
    