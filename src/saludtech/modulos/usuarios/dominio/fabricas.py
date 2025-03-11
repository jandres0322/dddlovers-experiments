import uuid
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from saludtech.modulos.usuarios.dominio.entidades import Usuario
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.modulos.usuarios.aplicacion.mapeadores import UsuarioMapeador

class FabricaEntregaImagen(Fabrica):

    """ def crear_objeto(usuario, UsuarioMapeador) -> Usuario:

        fecha_disponible = datetime.utcnow()

        return EntregaImagen(
            imagen_id=imagen_id,
            usuario_id=usuario_id,
            datos_entrega=ov.DatosEntrega(
                url_descarga=url_descarga,
                fecha_disponible=fecha_disponible,
                estado=ov.EstadoEntrega.DISPONIBLE
            )
        ) """
