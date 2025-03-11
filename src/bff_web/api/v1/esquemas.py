import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


SALUDTECH_HOST = os.getenv("SALUDTECH_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_imagenes(root) -> typing.List["Imagenes"]:
    imagenes_json = requests.get(f'http://{SALUDTECH_HOST}:5000/standard').json()
    imagenes = []

    for imagen in imagenes_json:
        imagenes.append(
            Imagenes(
                url_descarga=imagen.get('url_descarga'), 
                fecha_disponible=datetime.strptime(imagen.get('fecha_disponible'), FORMATO_FECHA), 
                id=imagen.get('imagen_id'), 
                id_usuario=imagen.get('usuario_id')
            )
        )

    return imagenes

@strawberry.type
class Itinerario:
    # TODO Completar objeto strawberry para incluir los itinerarios
    ...

@strawberry.type
class Imagenes:
    id: str
    id_usuario: str
    fecha_disponible: datetime
    url_descarga: str

@strawberry.type
class ImagenesRespuesta:
    mensaje: str
    codigo: int






