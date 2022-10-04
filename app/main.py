from os import getenv

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import database
import models
import schemas

app = FastAPI()


@app.post("/papers")
async def create_paper(paper: schemas.CreatePaper, db=Depends(database.get_db)):
    new_paper = models.Paper()
    print(new_paper)
    return


@app.get("/papers")
async def read_papers(
    db: Session = Depends(database.get_db), response_model=list[schemas.ReadPaper]
):
    papers = db.query(models.Paper).all()
    return papers


@app.get("/papers/{id}")
async def read_paper():
    pass


@app.patch("/papers/{id}")
async def update_paper():
    pass


@app.delete("/papers/{id}")
async def delete_paper():
    pass


if __name__ == "__main__":
    port = getenv("backend_port")
    uvicorn.run("main:app", port=port)
