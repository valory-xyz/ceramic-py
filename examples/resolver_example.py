from typing import Any, Dict

from graphene import Schema

from ceramic.compose.document import DocumentObject
from ceramic.compose.graphiql import create_graphiql_server

runtime = {
    "models": {
        "User": {
            "id": "<STREAM_ID>",
            "accountRelation": {"type": "single"},
        },
        "Metadata": {
            "id": "<STREAM_ID>",
            "accountRelation": {"type": "single"},
        },
    },
    "objects": {
        "User": {
            "age": {"type": "integer", "required": True},
            "name": {"type": "string", "required": True},
        },
        "Metadata": {
            "height": {"type": "integer", "required": True},
            "width": {"type": "integer", "required": True},
        },
    },
    "enums": {},
    "accountData": {
        "user": {"type": "node", "name": "User"},
        "metadata": {"type": "node", "name": "Metadata"},
    },
}

# Define data loaders.


def load_user(*args, **kwargs) -> Dict[str, Any]:
    """Load user data."""
    return {"id": "0xUSER", "age": 32, "name": "Viraj"}


def load_metadata(*args, **kwargs) -> Dict[str, Any]:
    """Load user data."""
    return {"id": "0xMETADATA", "height": 32, "width": 32}


user = DocumentObject(
    runtime=runtime,
)
Document = user.to_graphene(
    data_loaders={
        "User": load_user,
        "Metadata": load_metadata,
    }
)
schema = Schema(query=Document)
app = create_graphiql_server(
    query=Document,
)
