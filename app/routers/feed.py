from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import database, models, schemas

router = APIRouter(prefix="")


@router.get("/search", response_model=list[schemas.ResponsePaper])
async def read_papers(
    filter: schemas.FilterParameters, db: Session = Depends(database.get_db)
):
    # HACK kinda ugly
    filter_dict = {k: v for (k, v) in filter.dict().items() if v is not None}
    author = None
    if "author" in filter_dict:
        author = filter_dict["author"]
        del filter_dict["author"]
    print(author)
    papers = db.query(models.Paper).filter_by(**filter_dict)
    if author is not None:
        papers = papers.filter(models.Paper.authors.any(models.Author.name == author))
    return papers.all()
