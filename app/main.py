from multiprocessing import synchronize
from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import Session

from . import database, models, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.post("/papers")
async def create_paper(
    paper: schemas.BasePaper, db: Session = Depends(database.get_db)
):

    author_exists = (
        db.query(models.Author).filter_by(id=paper.author_id).first() is not None
    )
    if not author_exists:
        new_author = models.Author(id=paper.author_id)
        db.add(new_author)

    venue_exists = (
        db.query(models.Venue).filter_by(id=paper.venue_id).first() is not None
    )
    if not venue_exists:
        new_venue = models.Venue(id=paper.venue_id)
        db.add(new_venue)

    new_paper = models.Paper(**paper.dict())
    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)
    # TODO log paper
    return new_paper


@app.get("/papers")
async def read_papers(
    db: Session = Depends(database.get_db), response_model=list[schemas.BasePaper]
):
    papers = db.query(models.Paper).all()
    return papers


@app.get("/papers/{id}")
async def read_paper(
    id: str, db: Session = Depends(database.get_db), response_model=schemas.BasePaper
):

    paper = db.query(models.Paper).filter(models.Paper.id == id).first()
    if paper is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Paper with id "{id}" does not exist',
        )
    return paper


@app.patch("/papers/{id}")
async def update_paper(
    id: str, paper: schemas.UpdatePaper, db: Session = Depends(database.get_db)
):
    query = db.query(models.Paper).filter(models.Paper.id == id)
    existing_paper = query.first()
    if existing_paper is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Paper with id "{id}" does not exist',
        )
    query.update(paper.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return query.first()


@app.delete("/papers/{id}")
async def delete_paper(
    id: str, db: Session = Depends(database.get_db), response_model=schemas.BasePaper
):
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
