from pydantic import BaseModel, constr


class Author(BaseModel):
    id: constr(max_length=24)
    name: str
    organization: str

    class Config:
        orm_mode = True


class BasePaper(BaseModel):
    __tablename__ = "papers"
    venue_id: constr(max_length=24) | None

    citation_number: int | None
    year: int | None
    page_start: int | None
    page_end: int | None
    publisher: constr(max_length=50) | None
    issue: int | None
    volume: int | None
    language: constr(max_length=3) | None
    issn: constr(max_length=9) | None
    isbn: constr(max_length=30) | None
    doi: constr(max_length=50) | None
    pdf_url: constr(max_length=200) | None
    cluster: constr(max_length=32) | None
    authors: list[Author] = []

    class Config:
        orm_mode = True


class ResponsePaper(BasePaper):
    id: constr(max_length=24)
