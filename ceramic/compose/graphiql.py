import asyncio

import graphene
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from typing import Type


class Subscription(graphene.ObjectType):
    """Subscription count."""

    count = graphene.Int(upto=graphene.Int())

    async def subscribe_count(
        root,
        info: graphene.ResolveInfo,
        upto: int = 3,
    ) -> None:
        """Subsctibe and wait.

        :param root: Parameter help
        :type root: Subscription
        :param info: Parameter help
        :type info: graphene.ResolveInfo
        :param upto: Parameter help
        :type upto: int
        :return: RETURN INFO
        :rtype: AsyncIterator[int]
        """
        for i in range(upto):
            yield i
            await asyncio.sleep(1)


def create_graphiql_server(query: Type[graphene.ObjectType]) -> Starlette:
    """Create GraphiQL server.

    :param query: Query object
    :type query: graphene.ObjectType
    :return: Starlette application
    :rtype: Starlette
    """
    app = Starlette()
    schema = graphene.Schema(
        query=query,
        subscription=Subscription,
    )
    app.mount(
        "/",
        GraphQLApp(
            schema,
            on_get=make_graphiql_handler(),
        ),
    )
    return app
