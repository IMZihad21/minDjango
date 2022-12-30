import graphene
import graphql_jwt


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(graphene.ObjectType):
    token = graphql_jwt.ObtainJSONWebToken.Field()
    refresh = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
