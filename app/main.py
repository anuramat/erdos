from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import database, models
from app.routers import papers, auth, feed

models.Base.metadata.create_all(bind=database.engine)
# TODO remove when alembic is ready

app = FastAPI()
app.include_router(papers.router)
app.include_router(auth.router)
app.include_router(feed.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return "index path, nothing here"
