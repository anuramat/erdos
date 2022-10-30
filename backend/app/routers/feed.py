from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import database, models, schemas, oauth2

router = APIRouter(prefix="", tags=["Papers"])


@router.get("/search", response_model=list[schemas.ResponsePaper])
async def read_papers(
    filter: schemas.FilterParameters = Depends(),
    user_id: int = Depends(oauth2.verify_token),
    db: Session = Depends(database.get_db),
):
    # HACK ugly
    author = filter.author
    filter_dict = {
        k: v for (k, v) in filter.dict().items() if v is not None and k != "author"
    }
    papers = db.query(models.Paper).filter_by(**filter_dict)
    if author is not None:
        papers = papers.filter(models.Paper.authors.any(models.Author.name == author))
    return papers.all()
