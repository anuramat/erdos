from pydantic import BaseModel as BaseModel, constr, validator, Field
import typing


class Author(BaseModel):
    id: constr(max_length=24)
    name: str
    organization: str

    class Config:
        orm_mode = True


class Abstract(BaseModel):
    abstract: str | None
    indexed: dict | None

    class Config:
        orm_mode = True


class BasePaper(BaseModel):
    id: constr(max_length=24)
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
    abstract: Abstract | None

    class Config:
        orm_mode = True


class ResponsePaper(BasePaper):
    authors: list[Author] = []
    cluster: constr(max_length=32)


class FilterParameters(BaseModel):
    author: constr(strip_whitespace=True) | None
    year: int | constr(strip_whitespace=True) | None
    cluster: str | None
    venue: str | None

    @validator("year", pre=True)
    def empty_year_to_none(cls, v):
        if v == "":
            return None
        return v

    @validator("author", pre=True)
    def empty_author_to_none(cls, v):
        if v == "":
            return None
        return v


# TODO add strip_whitespace=True to constr fields
