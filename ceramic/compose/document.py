"""Document represensation of ComposeDB runtime"""

from typing import Any, Callable, Dict, Tuple, Type, cast

from graphene import Field, Int, List, ObjectType, String
from graphene.types.field import Field
from graphene.types.unmountedtype import UnmountedType
from graphql.type.definition import GraphQLResolveInfo

type_def_to_graphene_type: Dict[str, Type[UnmountedType]] = {
    "integer": Int,
    "string": String,
}


def snake_to_camel_case(string: str) -> str:
    """
    Conver snake case to camel case.

    :param string: String in snake case.
    :type string: str
    :return: String in camel case.
    :rtype: str
    """
    first, *rest = string.split("_")
    return "".join([first.lower(), *list(map(lambda x: x.lower().title(), rest))])


class IndexObject:
    """
    Index representation of the data models.
    """

    def __init__(self, name: str, type_obj: Dict) -> None:
        """
        Initialize IndexObject.

        :param name: Name of the index object.
        :type name: str
        :param type_obj: Type object of the index.
        :type type_obj: Dict
        """
        self.name = name
        self.type_obj = type_obj

        self._id = f"{self.name.lower()}Index"

    @property
    def id(self) -> str:
        """
        Get the ID of the index.

        :return: ID of the index.
        :rtype: str
        """
        return self._id

    def create_node(self) -> Type[ObjectType]:
        """
        Create data resolver node.

        :return: Created data resolver node.
        :rtype: Type[ObjectType]
        """
        type_defs = {}
        type_defs["id"] = String(required=True)
        for _name, _type_def in self.type_obj.items():
            type_defs[_name] = cast(
                UnmountedType, type_def_to_graphene_type.get(_type_def["type"])
            )(required=_type_def.get("required", False))
        return type(
            f"{self.name}Node",
            (ObjectType,),
            type_defs,
        )

    def create(
        self, data_loader: Callable[[], Dict[str, Any]]
    ) -> Tuple[Type[ObjectType], Callable[[], ObjectType]]:
        """
        Convert to graphene object.

        :param data_loader: Data loader function.
        :type data_loader: Callable[[], Dict[str, Any]]
        :return: Tuple containing the graphene object and data loader function.
        :rtype: Tuple[Type[ObjectType], Callable[[], ObjectType]]
        """
        Node = self.create_node()
        Edge = type(
            f"{self.name}Edge",
            (ObjectType,),
            {
                "node": Field(Node),
            },
        )
        Index = type(
            f"{self.name}Index",
            (ObjectType,),
            {
                "edges": List(of_type=Edge),
            },
        )

        def index_resolver(
            root, info: GraphQLResolveInfo, *args: Any, **kwargs: Any
        ) -> ObjectType:
            """
            Resolve index.

            :param root: Root object.
            :param info: GraphQL ResolveInfo object.
            :param args: Additional arguments.
            :param kwargs: Additional keyword arguments.
            :return: Resolved index object.
            :rtype: ObjectType
            """
            return Index(
                edges=[
                    Edge(
                        node=Node(**data_loader(*args, root=root, info=info, **kwargs))
                    )
                ]
            )

        return Index, index_resolver


class DocumentObject:
    """
    Document representation of runtime schema.
    """

    def __init__(self, runtime: Dict[str, Dict[str, Any]]) -> None:
        """
        Initialize DocumentObject.

        :param runtime: Runtime schema.
        :type runtime: Dict[str, Dict[str, Any]]
        """
        self.models = runtime["models"]
        self.objects = runtime["objects"]
        self.enums = runtime["enums"]
        self.account_data = runtime["accountData"]

    def to_graphene(
        self, data_loaders: Dict[str, Callable[[], Dict[str, Any]]]
    ) -> Type[ObjectType]:
        """
        Convert to graphene object.

        :param data_loaders: Data loaders.
        :type data_loaders: Dict[str, Callable[[], Dict[str, Any]]]
        :return: Graphene object.
        :rtype: Type[ObjectType]
        """
        _dict = {}
        for name, obj_def in self.objects.items():
            obj_index = IndexObject(
                name=name,
                type_obj=obj_def,
            )
            Index, data_loader = obj_index.create(
                data_loader=data_loaders.get(
                    name,
                )
            )
            _dict[obj_index.id] = Field(
                Index,
                first=Int(required=True),
            )
            _dict[f"resolve_{obj_index.id}"] = data_loader
        return type("Document", (ObjectType,), _dict)
