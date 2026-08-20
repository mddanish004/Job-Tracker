from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database.session import get_session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyResponse, CompanyUpdate
from app.services import company_service
from fastapi import APIRouter, Depends, HTTPException, status, Response


router = APIRouter()

@router.get("/companies/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, session=Depends(get_session)):
    company = company_service.get_company(session, company_id)
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return company

@router.post("/companies", response_model=CompanyResponse)
def create_company(company_data: CompanyCreate, session: Session = Depends(get_session)):
    return company_service.create_company(session,company_data,)
    
    
@router.get("/companies")
def get_companies(session: Session = Depends(get_session)):
    return company_service.get_companies(session)

@router.patch(
    "/companies/{company_id}",
    response_model=CompanyResponse,
)
def update_company(
    company_id: int,
    company_data: CompanyUpdate,
    session: Session = Depends(get_session),
):
    company = company_service.get_company(
        session,
        company_id,
    )

    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return company_service.update_company(
        session,
        company,
        company_data,
    )
    

@router.delete(
    "/companies/{company_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_company(
    company_id: int,
    session: Session = Depends(get_session),
):
    company = company_service.get_company(
        session,
        company_id,
    )

    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    company_service.delete_company(
        session,
        company,
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)