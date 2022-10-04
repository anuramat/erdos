from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pg_user = getenv("POSTGRES_USER")
pg_pass = getenv("POSTGRES_PASSWORD")
pg_host = "db"
pg_db = getenv("POSTGRES_DB")

url = f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}/{pg_db}"
engine = create_engine(url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
