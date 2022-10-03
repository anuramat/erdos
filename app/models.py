from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from .database import Base


class Paper(Base):
    __tablename__ = "papers"
    id = Column(String(24), primary_key=True)

    author_id = Column(String(24), ForeignKey("authors.id", ondelete="CASCADE"))
    author = relationship("Author")

    venue_id = Column(String(24), ForeignKey("venues.id", ondelete="CASCADE"))
    venue = relationship("Venue")

    doc_type = Column(String(50))
    # how will we update this? trigger on every new paper?
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
    paper_id = Column(String(24), ForeignKey("papers.id", ondelete="CASCADE"))
    abstract = Column(Text)
    indexed = Column(JSON)


class PaperFieldOfStudy(Base):
    __tablename__ = "paper_fields_of_study"
    paper_id = Column(String(24), ForeignKey("papers.id", ondelete="CASCADE"))
    field_of_study = Column(String(50))


class PaperKeyword(Base):
    __tablename__ = "paper_keywords"
    paper_id = Column(String(24), ForeignKey("papers.id", ondelete="CASCADE"))
    keyword = String(24)


class References(Base):
    __tablename__ = "references"
    paper_id = Column(String(24), ForeignKey("papers.id", ondelete="CASCADE"))
    referenced_id = Column(String(24), ForeignKey("papers.id"))


class ExternalLink(Base):
    __tablename__ = "external_links"
    paper_id = Column(String(24), ForeignKey("papers.id", ondelete="CASCADE"))
    link = Column(String(200))


# class User(Base):
#     id
#     username
#     author_id
#     password_hash
#     password_salt
