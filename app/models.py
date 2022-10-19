from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Text, Table
from sqlalchemy.orm import relationship

from app.database import Base


PaperAuthors = Table(
    "paper_authors",
    Base.metadata,
    Column(
        "paper_id",
        String(24),
        ForeignKey("papers.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "author_id",
        String(24),
        ForeignKey("authors.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

References = Table(
    "references",
    Base.metadata,
    Column(
        "paper_id",
        String(24),
        ForeignKey("papers.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "referenced_id",
        String(24),
        ForeignKey("papers.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Paper(Base):
    __tablename__ = "papers"
    id = Column(String(24), primary_key=True)

    venue_id = Column(String(24), ForeignKey("venues.id", ondelete="CASCADE"))

    citation_number = Column(Integer)
    year = Column(Integer)
    page_start = Column(Integer)
    page_end = Column(Integer)
    publisher = Column(String(50))
    issue = Column(Integer)
    volume = Column(Integer)
    language = Column(String(3))
    issn = Column(String(9))
    isbn = Column(String(30))
    doi = Column(String(50))
    pdf_url = Column(String(200))
    cluster = Column(String(32))

    external_links = relationship("ExternalLink")
    fields_of_study = relationship("PaperFieldOfStudy")
    keyword = relationship("PaperKeyword")
    abstract = relationship("Abstract")
    venue = relationship("Venue")
    authors = relationship("Author", secondary=PaperAuthors)
    # TODO references many-to-many self referencing


class Author(Base):
    __tablename__ = "authors"
    id = Column(String(24), primary_key=True)
    name = Column(Text)
    organization = Column(Text)


class Venue(Base):
    __tablename__ = "venues"
    id = Column(String(24), primary_key=True)
    name = Column(Text)


class Abstract(Base):
    __tablename__ = "abstracts"
    paper_id = Column(
        String(24), ForeignKey("papers.id", ondelete="CASCADE"), primary_key=True
    )
    abstract = Column(Text)
    indexed = Column(JSON)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    hash = Column(String(128), nullable=False)
    salt = Column(String(128), nullable=False)
    author_id = Column(
        String(24), ForeignKey("authors.id", ondelete="CASCADE"), nullable=False
    )
    author = relationship("Author")


class PaperFieldOfStudy(Base):
    __tablename__ = "paper_fields_of_study"
    id = Column(Integer, primary_key=True)

    paper_id = Column(
        String(24), ForeignKey("papers.id", ondelete="CASCADE"), nullable=False
    )
    field_of_study = Column(String(50), nullable=False)


class PaperKeyword(Base):
    __tablename__ = "paper_keywords"
    id = Column(Integer, primary_key=True)

    paper_id = Column(
        String(24), ForeignKey("papers.id", ondelete="CASCADE"), nullable=False
    )
    keyword = Column(String(24), nullable=False)


class ExternalLink(Base):
    __tablename__ = "external_links"
    id = Column(Integer, primary_key=True)

    paper_id = Column(
        String(24), ForeignKey("papers.id", ondelete="CASCADE"), nullable=False
    )
    link = Column(String(200), nullable=False)
