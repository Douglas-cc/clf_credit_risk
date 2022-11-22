from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models
from service.classifier import Serving


class RepositorieClassifier:
    def __init__(self, db: Session):
        self.db = db
        self.serving = Serving()
        
        
    def create(self, data: schemas.InputData):
        output = self.serving.classifier(
            data.income,
            data.age,
            data.loan
        )
        
        save = models.Classification(
            income = data.income,
            name = data.name,
            age = data.age,
            loan = data.loan,
            predict = output,
            date = data.date
        )
        
        self.db.add(save)
        self.db.commit()
        self.db.refresh(save)    
        return save
    
    
    def ready(self):
        query = select(models.Classification)
        return self.db.execute(query).scalars().all()
    
    
    def search(self, name: str):
        query = select(models.Classification).where(
            models.Classification.name == name
        )
        
        return self.db.execute(query).scalars().all() 
    