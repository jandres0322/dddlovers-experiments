from seedwork.aplicacion.dto import Mapeador
from saludtech.modulos.imagenes.dominio.entidades import EntregaImagen, HistorialEntrega
from saludtech.modulos.imagenes.aplicacion.dto import EntregaImagenDTO, HistorialEntregaDTO, RegistroDescargaDTO

class MapeadorEntregaImagen(Mapeador):

    def externo_a_dto(self, entrega: EntregaImagen) -> EntregaImagenDTO:
        return EntregaImagenDTO(
            id_entrega=entrega.id,
            imagen_id=entrega.imagen_id,
            estado=entrega.datos_entrega.estado.value,
            url_descarga=entrega.datos_entrega.url_descarga
        )

    def dto_a_externo(self, dto: EntregaImagenDTO) -> EntregaImagen:
        raise NotImplementedError("No se admite la conversión de DTO a entidad en este contexto.")

class HistorialEntregaHandler(Mapeador):

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
        raise NotImplementedError("No se admite la conversión de DTO a entidad en este contexto.")
