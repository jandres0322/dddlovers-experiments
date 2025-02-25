from dataclasses import dataclass, field
from datetime import datetime
import uuid
from seedwork.dominio.entidades import AgregacionRaiz, Entidad
from saludtech.modulos.imagenes.dominio import objetos_valor as ov
from saludtech.modulos.imagenes.dominio.eventos import EntregaImagenDisponible, ImagenDescargada

@dataclass
class EntregaImagen(AgregacionRaiz):

    imagen_id: uuid.UUID
    usuario_id: uuid.UUID
    datos_entrega: ov.DatosEntrega = field(default_factory=lambda: ov.DatosEntrega("", datetime.utcnow(), ov.EstadoEntrega.DISPONIBLE, False))  # Autorización por defecto: False

    def validar_entrega(self):
        if self.datos_entrega.estado != ov.EstadoEntrega.DISPONIBLE:
            raise ValueError(f"La imagen {self.imagen_id} aún no está disponible para entrega.")

        self.agregar_evento(EntregaImagenDisponible(
            id_entrega=str(self.id),
            imagen_id=str(self.imagen_id),
            usuario_id=str(self.usuario_id),
            url_descarga=self.datos_entrega.url_descarga,
            fecha_disponible=self.datos_entrega.fecha_disponible,
            estado=self.datos_entrega.estado,
            autorizado=True
        ))

@dataclass
class HistorialEntrega(AgregacionRaiz):

    entrega_id: uuid.UUID
    registros_descarga: list[ov.RegistroDescarga] = field(default_factory=list)

    def registrar_descarga(self, usuario_id: uuid.UUID):
        nuevo_registro = ov.RegistroDescarga(usuario_id, datetime.utcnow())
        self.registros_descarga.append(nuevo_registro)

        self.agregar_evento(ImagenDescargada(
            id_entrega=str(self.entrega_id),
            usuario_id=str(usuario_id),
            fecha_descarga=nuevo_registro.fecha_descarga,
            autorizado=True
        ))
