import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from saludtech.modulos.imagenes.dominio.excepciones import ImagenNoDisponible, DescargaNoRegistrada
from datetime import datetime

class ValidarDisponibilidadMixin:
    """Mixin para validar que una imagen está disponible para entrega."""

    def validar_disponibilidad(self):
        """Verifica que la imagen esté lista para entrega y que no haya expirado."""
        if self.datos_entrega.estado != ov.EstadoEntrega.DISPONIBLE:
            raise ImagenNoDisponible(self.imagen_id)

class GestionarEstadoEntregaMixin:
    """Mixin para gestionar cambios de estado en la entrega de imágenes."""

    def cambiar_estado_entrega(self, nuevo_estado: ov.EstadoEntrega):
        """Cambia el estado de la entrega asegurando que solo se usen estados permitidos."""
        estados_permitidos = {ov.EstadoEntrega.DISPONIBLE, ov.EstadoEntrega.EXPIRADA, ov.EstadoEntrega.ERROR}
        if nuevo_estado not in estados_permitidos:
            raise ValueError(f"Estado de entrega '{nuevo_estado}' no permitido.")

        self.datos_entrega = self.datos_entrega.__class__(
            url_descarga=self.datos_entrega.url_descarga,
            fecha_disponible=self.datos_entrega.fecha_disponible,
            estado=nuevo_estado
        )

        # Agregar lógica para registrar cambios de estado si es necesario
        if nuevo_estado == ov.EstadoEntrega.EXPIRADA:
            print(f"La entrega de la imagen {self.imagen_id} ha expirado.")

class RegistroDescargaMixin:
    """Mixin para gestionar el registro de descargas en el historial de entrega."""

    def registrar_descarga(self, usuario_id: str):
        """Registra una nueva descarga en la lista de historial."""
        if not hasattr(self, 'registros_descarga'):
            raise DescargaNoRegistrada(self.entrega_id)

        nueva_descarga = {"usuario_id": usuario_id, "fecha_descarga": datetime.utcnow()}
        self.registros_descarga.append(nueva_descarga)

        # Agregar lógica si se quiere notificar sobre la descarga
        print(f"Usuario {usuario_id} descargó la imagen {self.entrega_id} en {nueva_descarga['fecha_descarga']}.")
