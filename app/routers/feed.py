from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import database, models, schemas

router = APIRouter(prefix="")


@router.get("/search", response_model=list[schemas.ResponsePaper])
async def read_papers(
    filter: schemas.FilterParameters = Depends(),
    db: Session = Depends(database.get_db),
):
    # HACK ugly
    filter_dict = {k: v for (k, v) in filter.dict().items() if v is not None}
    papers = db.query(models.Paper).filter_by(**filter_dict)
    return papers.all()
