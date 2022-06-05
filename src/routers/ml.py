import os 
import traceback
from loguru import logger 
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from schemas.schemas import InputData
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repositories.ml import RepositorieClassifier


router = APIRouter()


@router.get('/classified')
async def list_classification(db: Session = Depends(get_db)):
    classifications = RepositorieClassifier(db).ready()
    if not classifications:
        raise HTTPException(status_code = 404, detail='No classifications saved')
    return classifications

@router.get('/classified/{name}')
async def search_name(name: str, db: Session = Depends(get_db)):
    select_name = RepositorieClassifier(db).search(name)
    if not select_name:
        raise HTTPException(status_code = 404, detail='No classifications saved with name')
    return select_name 
    
@router.post('/classified')
async def classified(data: InputData, db: Session = Depends(get_db)):
    try:
        output = RepositorieClassifier(db).create(data)
        logger.info(f'Resultado: {output.predict}')
        
        if output.predict == 0:
            return f'Não existe risco conceder credito a {output.name}' 
        else:
            return f'Existe risco de conceder credito a {output.name}' 
    
    except Exception as e:
        logger.debug(traceback.format_exc())
        raise HTTPException(
            status_code=500, 
            detail="Exceptions can't be handheld by a teapot"
        )

