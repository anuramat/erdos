from pydantic import BaseModel, EmailStr, constr, validator
from app.models import Abstract


class Author(BaseModel):
    id: constr(max_length=24)
    name: str | None
    organization: str | None

    class Config:
        orm_mode = True


class Abstract(BaseModel):
    text: str
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
    author_ids: list[constr(max_length=24)] = []

    class Config:
        orm_mode = True


class ResponsePaper(BasePaper):
    tag: constr(max_length=32)
    authors: list[Author] = []


class FilterParameters(BaseModel):
    """
    search parameter
    """

    author: constr(strip_whitespace=True) | None
    year: int | constr(strip_whitespace=True) | None
    tag: str | None
    venue: str | None

    @validator("*", pre=True)
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v

    # todo make sure year is not str


# TODO add strip_whitespace=True to constr fields


class UserData(BaseModel):
    """
    stuff stored in JWT
    """

    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreds(BaseModel):
    """
    request body for login/registration
    """

    email: EmailStr
    password: str


class BaseAuthor(BaseModel):
    id: constr(max_length=24)
    name: str | None
    organization: str | None

    class Config:
        orm_mode = True


class ResponseAuthor(BaseAuthor):
    rating: int

    class Config:
        orm_mode = True
