from pydantic import BaseModel, constr


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


class BasePaper(UpdatePaper):
    id: constr(max_length=24)
