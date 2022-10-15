from fastapi import Depends, FastAPI

from app import database, models
from app.routers import papers, users

models.Base.metadata.create_all(bind=database.engine)
# TODO remove when alembic is ready

app = FastAPI()
app.include_router(papers.router)
app.include_router(users.router)


@app.get("/")
async def index():
    return "index path, nothing here"
