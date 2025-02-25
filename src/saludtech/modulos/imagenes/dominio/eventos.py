from dataclasses import dataclass
from datetime import datetime
from saludtech.seedwork.dominio.eventos import EventoDominio
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
import uuid

@dataclass
class EntregaImagenDisponible(EventoDominio):

    id_entrega: uuid.UUID = None
    imagen_id: uuid.UUID = None
    usuario_id: uuid.UUID = None
    url_descarga: str = None
    fecha_disponible: datetime = None
    estado: ov.EstadoEntrega = ov.EstadoEntrega.DISPONIBLE

@dataclass
class ImagenDescargada(EventoDominio):

    id_entrega: uuid.UUID = None
    usuario_id: uuid.UUID = None
    fecha_descarga: datetime = None
