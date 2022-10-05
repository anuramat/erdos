from pydantic import BaseModel, constr


class BasePaper(BaseModel):
    __tablename__ = "papers"
    id: constr(max_length=24)
    author_id: constr(max_length=24)
    venue_id: constr(max_length=24)

    citation_number: int
    year: int
    page_start: int
    page_end: int
    publisher: constr(max_length=50)
    issue: int
    volume: int
    language: constr(max_length=3)
    issn: constr(max_length=9)
    isbn: constr(max_length=30)
    doi: constr(max_length=50)
    pdf_url: constr(max_length=200)

    class Config:
        orm_mode = True


class UpdatePaper(BaseModel):
    __tablename__ = "papers"
    author_id: constr(max_length=24) | None
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

    class Config:
        orm_mode = True
