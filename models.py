from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

movie_genre = db.Table('movie_genre',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Genre(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255))

class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255))
    description: Mapped[str] = mapped_column(db.String(255))
    release_year: Mapped[int] = mapped_column(db.Integer)
    genres: Mapped[List["Genre"]] = db.relationship(secondary=movie_genre, backref=db.backref('genres'), lazy='subquery')
