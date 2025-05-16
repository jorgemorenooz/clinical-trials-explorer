from pydantic import BaseModel
from datetime import date

class ClinicalTrialBase(BaseModel):
    # id will be added in the response schema
    official_title: str
    acronym: str | None = None
    disease_area: str
    trial_phase: str
    status: str
    start_date: date
    end_date: date
    country: str
    sponsor: str
    description: str | None = None

class ClinicalTrialCreate(ClinicalTrialBase):
    """Used for POST requests"""
    pass

class ClinicalTrial(ClinicalTrialBase):
    """Used for GET requests"""
    id: int
    
    class Config:
        from_attributes = True
        
class DeleteResponse(BaseModel):
    message: str