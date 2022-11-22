from sqlalchemy import Column, Integer, String, Float, DateTime
from infra.sqlalchemy.config.database import Base

class Classification(Base):
    __tablename__ = "tbl_predict"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    income = Column(Float)
    age = Column(Float)
    loan = Column(Float)
    predict = Column(Float)  
    date = Column(DateTime)  
