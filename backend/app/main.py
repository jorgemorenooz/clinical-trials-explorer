from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.models import Base, ClinicalTrial
from app.database import get_db, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/trials", response_model=List[schemas.ClinicalTrial])
def get_trials(db: Session = Depends(get_db)):
    """
    Retrieve all clinical trial records from the database.
    
    Args:
        db (Session): SQLAlchemy database session provided via FastAPI dependency injection.

    Returns:
        List[ClinicalTrial]: A list of all clinical trials stored in the database.
    """
     
    return db.query(ClinicalTrial).all()

@app.get("/trials/{id}", response_model=schemas.ClinicalTrial)
def get_trial(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single clinical trial from the database by its ID.

    Args:
        id (int): ID from the trial wanted.
        db (Session): Database session (injected via dependency).

    Returns:
        ClinicalTrial: The retrieved trial.
    """
    
    existing_trial = db.query(ClinicalTrial).filter(ClinicalTrial.id == id).first()
    if existing_trial is None:
        raise HTTPException(status_code=404, detail="Trial not found")
    
    return existing_trial

@app.post("/trials", response_model=schemas.ClinicalTrial)
def create_trial(trial: schemas.ClinicalTrialCreate, db: Session = Depends(get_db)):
    """
    Create a new clinical trial record in the database.

    Args:
        trial (ClinicalTrialCreate): Incoming validated request data.
        db (Session): Database session (injected via dependency).

    Returns:
        ClinicalTrial: The created trial, including its generated ID.
    """
    
    db_trial = ClinicalTrial(**trial.model_dump())
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    
    return db_trial

@app.put("/trials/{id}", response_model=schemas.ClinicalTrial)
def update_trial(id: int, trial: schemas.ClinicalTrialCreate, db: Session = Depends(get_db)):
    """
    Update a clinical trial by its ID.

    Args:
        id (int): Trial ID.
        trial (ClinicalTrialCreate): New data to update with.
        db (Session): DB session.

    Returns:
        ClinicalTrial: The updated trial.
    """
    existing_trial = db.query(ClinicalTrial).filter(ClinicalTrial.id == id).first()
    if existing_trial is None:
        raise HTTPException(status_code=404, detail="Trial not found")
    
    for key, value in trial.model_dump().items():
        setattr(existing_trial, key, value)

    db.commit()
    db.refresh(existing_trial)

    return existing_trial

@app.delete("/trials/{id}")
def delete_trial(id: int, db: Session = Depends(get_db)):
    """
    Delete a clinical trial by its ID.

    Args:
        id (int): Trial ID.
        db (Session): DB session.

    Returns:
        dict: Success message.
    """
    existing_trial = db.query(ClinicalTrial).filter(ClinicalTrial.id == id).first()
    if existing_trial is None:
        raise HTTPException(status_code=404, detail="Trial not found")

    db.delete(existing_trial)
    db.commit()

    return {"message": "Trial deleted"}
