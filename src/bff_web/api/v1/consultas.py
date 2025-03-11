
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    imagenes: typing.List[Imagenes] = strawberry.field(resolver=obtener_imagenes)