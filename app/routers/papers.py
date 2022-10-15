from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import database, models, schemas

router = APIRouter(prefix="/papers")


@router.post("/", response_model=schemas.BasePaper)
async def create_paper(
    paper_request: schemas.BasePaper, db: Session = Depends(database.get_db)
):

    author_exists = (
        db.query(models.Author).filter_by(id=paper_request.author_id).first()
        is not None
    )
    if not author_exists:
        new_author = models.Author(id=paper_request.author_id)
        db.add(new_author)

    venue_exists = (
        db.query(models.Venue).filter_by(id=paper_request.venue_id).first() is not None
    )
    if not venue_exists:
        new_venue = models.Venue(id=paper_request.venue_id)
        db.add(new_venue)

    new_paper = models.Paper(**paper_request.dict())
    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)
    return new_paper


@router.get("/", response_model=list[schemas.BasePaper])
async def read_papers(db: Session = Depends(database.get_db)):
    papers = db.query(models.Paper).all()
    return papers


@router.get("/{id}", response_model=schemas.BasePaper)
async def read_paper(id: str, db: Session = Depends(database.get_db)):

    paper = db.query(models.Paper).filter(models.Paper.id == id).first()
    if paper is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Paper with id "{id}" does not exist',
        )
    return paper


@router.patch("/{id}", response_model=schemas.BasePaper)
async def update_paper(
    id: str, paper_request: schemas.UpdatePaper, db: Session = Depends(database.get_db)
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


@router.delete("/{id}", response_model=schemas.BasePaper)
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
