import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, db
from models import Genre as GenreModel
from sqlalchemy.orm import Session

# ----- Movie Scehmas ----- #

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)

    def resolve_movies(self, info):
        return db.session.execute(db.select(MovieModel)).scalars()
    
class AddMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        release_year = graphene.Int(required=True)
        genres = graphene.List(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, title, description, release_year, genres):
        with Session(db.engine) as session:
            with session.begin():
                genres = session.execute(db.select(GenreModel).where(GenreModel.name.in_(genres))).scalars().all()
                print(genres)
                movie = MovieModel(title=title, description=description, release_year=release_year, genres=genres)
                session.add(movie)

            session.refresh(movie)
            return AddMovie(movie=movie)
        
class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        release_year = graphene.Int(required=True)
        genres = graphene.List(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, id, title, description, release_year):
        with Session(db.engine) as session:
            with session.begin():
                genres = session.execute(db.select(GenreModel).where(GenreModel.name.in_(genres))).scalars().all()
                print(genres)
                movie = session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()
                if movie:
                    movie.title = title
                    movie.description = description
                    movie.release_year = release_year
                    movie.genres = genres
                else:
                    return None

            session.refresh(movie)
            return UpdateMovie(movie=movie)
        
class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, id):
        with Session(db.engine) as session:
            with session.begin():
                movie = session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()
                if movie:
                    session.delete(movie)
                    return 'Deleted.'
                else:
                    return None
            session.refresh(movie)
            return DeleteMovie(movie=movie)
        
class Mutation(graphene.ObjectType):

    create_movie = AddMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()


