from dataclasses import dataclass
from datetime import datetime
from seedwork.dominio.eventos import EventoDominio
import objetos_valor as ov

@dataclass
class EntregaImagenDisponible(EventoDominio):

    id_entrega: str
    imagen_id: str
    usuario_id: str
    url_descarga: str
    fecha_disponible: datetime
    estado: ov.EstadoEntrega = ov.EstadoEntrega.DISPONIBLE

@dataclass
class ImagenDescargada(EventoDominio):

    id_entrega: str
    usuario_id: str
    fecha_descarga: datetime
