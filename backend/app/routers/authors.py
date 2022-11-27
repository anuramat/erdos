from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app import database, models, schemas
from app.logic import clusters

router = APIRouter(prefix="/authors", tags=["Authors stuff"])


@router.post("/", response_model=schemas.ResponseAuthor)
async def create_author(
    author_request: schemas.BaseAuthor,
    db: Session = Depends(database.get_db),
):
    author_exists = (
        db.query(models.Author).filter_by(id=author_request.id).first() is not None
    )
    if author_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Author with id {author_request.id} already exists",
        )
    new_author = models.Author(**author_request.dict(), rating=0)
    db.add(new_author)
    db.commit()
    return new_author


@router.get("/best/{page_num}", response_model=list[schemas.ResponseAuthor])
async def read_authors(page_num: int, db: Session = Depends(database.get_db)):
    """
    returns top 10 authors with given offset
    """
    if page_num < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect page number"
        )
    return (
        db.query(models.Author)
        .order_by(models.Author.rating)
        .offset((page_num - 1) * 10)
        .limit(10)
        .all()
    )
