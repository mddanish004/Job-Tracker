from sqlmodel import Session, select
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate



def get_company(session: Session, company_id: int):
    statement = select(Company).where(Company.id == company_id)
    
    company = session.exec(statement).first()
    
    return company


def update_company(
    session: Session,
    company: Company,
    company_data: CompanyUpdate,
):
    update_data = company_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(company, key, value)

    session.add(company)
    session.commit()
    session.refresh(company)

    return company


def get_companies(session):
    statement = select(Company)
    return session.exec(statement).all()


def create_company(session: Session, company_date: CompanyCreate):
    company = Company(
            name= company_date.name,
            website= company_date.website,
        )
        
    session.add(company)
    session.commit()
    session.refresh(company)
        
    return company

def delete_company(session: Session, company: Company):
    session.delete(company)
    session.commit()