from saludtech.seedwork.dominio.servicios import Servicio
from saludtech.modulos.imagenes.dominio.repositorios import RepositorioEntregaImagen, RepositorioHistorialEntrega
from saludtech.modulos.imagenes.dominio.entidades import HistorialEntrega
from saludtech.modulos.imagenes.dominio.objetos_valor import EstadoEntrega, RegistroDescarga
from saludtech.modulos.imagenes.dominio.reglas import ReglaEntregaDisponible
from saludtech.modulos.imagenes.dominio.excepciones import ImagenNoDisponible
from datetime import datetime
import uuid

class ServicioEntregaImagen(Servicio):

    def __init__(self, repositorio_entrega: RepositorioEntregaImagen):
        self.repositorio_entrega = repositorio_entrega

    def marcar_como_disponible(self, id_entrega: uuid.UUID):

        entrega = self.repositorio_entrega.obtener_por_id(id_entrega)
        if not entrega:
            raise ImagenNoDisponible(id_entrega)

        # Validación de disponibilidad
        self.validar_regla(ReglaEntregaDisponible(entrega.datos_entrega.estado))

        entrega.datos_entrega.estado = EstadoEntrega.DISPONIBLE
        self.repositorio_entrega.actualizar(entrega)

class ServicioRegistroDescarga(Servicio):

    def __init__(self, repositorio_historial: RepositorioHistorialEntrega):
        self.repositorio_historial = repositorio_historial

    def registrar_descarga(self, id_entrega: uuid.UUID, usuario_id: uuid.UUID):

        historial = self.repositorio_historial.obtener_por_id(id_entrega)
        if not historial:
            historial = HistorialEntrega(entrega_id=id_entrega, registros_descarga=[])

        nueva_descarga = RegistroDescarga(usuario_id=usuario_id, fecha_descarga=datetime.utcnow())
        historial.registros_descarga.append(nueva_descarga)

        self.repositorio_historial.actualizar(historial)
