import graphene
import schemas.movieSchema as movieSchema
import schemas.genreSchema as genreSchema

class Query(movieSchema.Query, genreSchema.Query, graphene.ObjectType):
    pass

class Mutation(movieSchema.Mutation, genreSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)