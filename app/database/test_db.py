from sqlmodel import Session, select

from app.database.connection import engine
from app.models.company import Company


with Session(engine) as session:
    statement = select(Company).where(Company.id==2)
    
    company = session.exec(statement).first()
    
    if company:
        session.delete(company)
        session.commit()
    
    
    
    
            