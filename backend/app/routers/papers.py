from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app import oauth2
from app import database, models, schemas
from app.logic import clusters

router = APIRouter(prefix="/papers", tags=["Basic CRUD"])


@router.post("/", response_model=schemas.ResponsePaper)
async def create_paper(
    paper_request: schemas.BasePaper,
    db: Session = Depends(database.get_db),
):
    paper_exists = (
        db.query(models.Paper).filter_by(id=paper_request.id).first() is not None
    )
    if paper_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Paper with id "{paper_request.id}" already exists',
        )
    venue_exists = (
        db.query(models.Venue).filter_by(id=paper_request.venue_id).first() is not None
    )
    if not venue_exists:
        new_venue = models.Venue(id=paper_request.venue_id)
        db.add(new_venue)

    abstract = models.Abstract(**paper_request.abstract.dict())
    authors = [models.Author(**i.dict()) for i in paper_request.authors]

    paper_dict = paper_request.dict()
    paper_dict["tag"] = clusters.get_tag(paper_request.abstract.text)
    del paper_dict["abstract"]
    del paper_dict["authors"]
    new_paper = models.Paper(**paper_dict, abstract=abstract, authors=authors)

    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)
    return new_paper


@router.get("/", response_model=list[schemas.ResponsePaper])
async def read_papers(db: Session = Depends(database.get_db)):
    return db.query(models.Paper).all()


@router.get("/{id}", response_model=schemas.ResponsePaper)
async def read_paper(id: str, db: Session = Depends(database.get_db)):

    paper = db.query(models.Paper).filter(models.Paper.id == id).first()
    if paper is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Paper with id "{id}" does not exist',
        )
    return paper


@router.patch("/{id}", response_model=schemas.ResponsePaper)
async def update_paper(
    id: str,
    paper_request: schemas.BasePaper,
    db: Session = Depends(database.get_db),
):
    query = db.query(models.Paper).filter(models.Paper.id == id)
    existing_paper = query.first()
    if existing_paper is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Paper with id "{id}" does not exist',
        )
    query.update(paper_request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return query.first()


@router.delete("/{id}")
async def delete_paper(id: str, db: Session = Depends(database.get_db)):
    query = db.query(models.Paper).filter(models.Paper.id == id)
    paper = query.first()
    if paper is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Paper with id "{id}" does not exist',
        )
    query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
