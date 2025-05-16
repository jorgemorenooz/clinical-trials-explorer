from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class ClinicalTrial(Base):
    __tablename__ = "clinical_trials"
    
    id = Column(Integer, primary_key=True, index=True)
    official_title = Column(String, nullable=False)
    acronym = Column(String, nullable=True)
    disease_area = Column(String, nullable=False)
    trial_phase = Column(String, nullable=False)
    status = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    sponsor = Column(String, nullable=False)
    description = Column(Text, nullable=True)