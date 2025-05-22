from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.models import Base, ClinicalTrial
from app.database import get_db, engine

app = FastAPI(
    title="Clinical Trials Explorer API",
    description="A FastAPI-based service to manage and explore EU clinical trial data.",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)


@app.get("/trials", tags=["Trials"])
def get_trials(
    disease_area: str = None,
    status: str = None,
    country: str = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    """
    Retrieve clinical trials with optional filtering and pagination.

    Args:
        disease_area (str, optional): Filter by disease area.
        status (str, optional): Filter by trial status.
        country (str, optional): Filter by country of origin.
        limit (int, optional): Maximum number of results to return (default: 10).
        offset (int, optional): Number of records to skip before starting to return results (default: 0).
        db (Session): SQLAlchemy database session.

    Returns:
        List[ClinicalTrial]: A list of clinical trials matching the filters and pagination.
    """
    query = db.query(ClinicalTrial)

    if disease_area:
        query = query.filter(ClinicalTrial.disease_area == disease_area)
    if status:
        query = query.filter(ClinicalTrial.status == status)
    if country:
        query = query.filter(ClinicalTrial.country == country)

    total_count = query.count()
    results = query.offset(offset).limit(limit).all()

    return {
        "total": total_count,
        "limit": limit,
        "offset": offset,
        "data": results
    }

@app.get(
    "/trials/{id}",
    response_model=schemas.ClinicalTrial,
    tags=["Trials"],
    summary="Retrieve a single clinical trial",
    description=" Retrieve a single clinical trial record in the database identified by its ID."
)
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

@app.post(
    "/trials",
    response_model=schemas.ClinicalTrial,
    tags=["Trials"],
    summary="Create a new trial",
    description="Creates a new clinical trial record in the database using provided trial data."
)
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

@app.put(
    "/trials/{id}",
    response_model=schemas.ClinicalTrial,
    tags=["Trials"],
    summary="Updates an existing trial",
    description="Updates an existing trial record in the database using provided trial data."
)
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

@app.delete(
    "/trials/{id}",
    tags=["Trials"],
    summary="Deletes an existing trial",
    description="Deletes an existing trial record in the database identified by its ID."
)
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
