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


class CreatePaper(BasePaper):
    pass


class ReadPaper(BasePaper):
    # TODO
    pass
