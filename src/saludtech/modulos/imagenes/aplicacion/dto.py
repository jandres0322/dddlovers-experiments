from dataclasses import dataclass
import uuid
from datetime import datetime
from seedwork.aplicacion.dto import DTO
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class EntregaImagenDTO(DTO):
    id_entrega: uuid.UUID
    imagen_id: uuid.UUID
    estado: str
    url_descarga: str

@dataclass(frozen=True)
class HistorialEntregaDTO(DTO):
    id_entrega: uuid.UUID
    registros: list[dict]

@dataclass(frozen=True)
class RegistroDescargaDTO(DTO):
    usuario_id: uuid.UUID
    fecha_descarga: datetime
