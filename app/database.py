from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import getenv

pg_user = getenv("POSTGRES_USER")
pg_pass = getenv("POSTGRES_PASSWORD")
pg_host = "db"
pg_db = getenv("POSTGRES_DB")
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}/{pg_db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
