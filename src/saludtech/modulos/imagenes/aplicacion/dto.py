from dataclasses import dataclass
import uuid
from datetime import datetime
from saludtech.seedwork.aplicacion.dto import DTO, Mapeador
from saludtech.modulos.imagenes.dominio.entidades import EntregaImagen, HistorialEntrega

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

class MapeadorEntregaImagen(Mapeador):

    def externo_a_dto(self, entrega: EntregaImagen) -> EntregaImagenDTO:
        return EntregaImagenDTO(
            id_entrega=entrega.id,
            imagen_id=entrega.imagen_id,
            estado=entrega.estado.value,
            url_descarga=entrega.url_descarga
        )

    def dto_a_externo(self, dto: EntregaImagenDTO) -> EntregaImagen:
        return dto.__dict__

class MapeadorHistorialEntrega(Mapeador):

    def externo_a_dto(self, historial: HistorialEntrega) -> HistorialEntregaDTO:
        registros_dto = [
            RegistroDescargaDTO(usuario_id=reg.usuario_id, fecha_descarga=reg.fecha_descarga)
            for reg in historial.registros_descarga
        ]
        return HistorialEntregaDTO(
            id_entrega=historial.entrega_id,
            registros=registros_dto
        )

    def dto_a_externo(self, dto: HistorialEntregaDTO) -> HistorialEntrega:
        return dto.__dict__
