from datetime import datetime
import uuid
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from saludtech.modulos.imagenes.dominio.entidades import EntregaImagen
from seedwork.dominio.fabricas import Fabrica

class FabricaEntregaImagen(Fabrica):
    """Fábrica para la creación de entregas de imágenes procesadas."""

    @staticmethod
    def crear_entrega(imagen_id: uuid.UUID, usuario_id: uuid.UUID, url_descarga: str) -> EntregaImagen:
        """Crea una entrega de imagen lista para su disponibilidad."""

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
