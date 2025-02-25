from datetime import datetime
import uuid
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from saludtech.modulos.imagenes.dominio.entidades import EntregaImagen
from saludtech.seedwork.dominio.fabricas import Fabrica

class FabricaEntregaImagen(Fabrica):

    @staticmethod
    def crear_entrega(imagen_id: uuid.UUID, usuario_id: uuid.UUID, url_descarga: str) -> EntregaImagen:

        fecha_disponible = datetime.utcnow()

        return EntregaImagen(
            imagen_id=imagen_id,
            usuario_id=usuario_id,
            datos_entrega=ov.DatosEntrega(
                url_descarga=url_descarga,
                fecha_disponible=fecha_disponible,
                estado=ov.EstadoEntrega.DISPONIBLE
            )
        )
