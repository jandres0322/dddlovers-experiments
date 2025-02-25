from seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.imagenes.aplicacion.comandos.marcar_disponible import (
    MarcarDisponible, MarcarDisponibleHandler
)
from saludtech.modulos.imagenes.aplicacion.comandos.registrar_descarga import (
    RegistrarDescarga, RegistrarDescargaHandler
)
from saludtech.modulos.imagenes.aplicacion.queries.obtener_entrega import (
    QueryObtenerEntrega, ManejadorObtenerEntrega
)
from saludtech.modulos.imagenes.aplicacion.queries.obtener_historial import (
    QueryObtenerHistorial, ManejadorObtenerHistorial
)
from saludtech.modulos.imagenes.aplicacion.dto import (
    EntregaImagenDTO, RegistroDescargaDTO, HistorialEntregaDTO
)
import uuid

class ServicioEntregaImagenApp(Servicio):

    def __init__(self, manejador_marcar_disponible: MarcarDisponibleHandler,
                 manejador_obtener_entrega: ManejadorObtenerEntrega):
        self.manejador_marcar_disponible = manejador_marcar_disponible
        self.manejador_obtener_entrega = manejador_obtener_entrega

    def marcar_imagen_disponible(self, entrega: EntregaImagenDTO):
        comando = MarcarDisponible(entrega=entrega)
        self.manejador_marcar_disponible.handle(comando)

    def obtener_entrega(self, id_entrega: uuid.UUID) -> EntregaImagenDTO:
        query = QueryObtenerEntrega(id_entrega=id_entrega)
        resultado = self.manejador_obtener_entrega.handle(query)
        return resultado.entrega if resultado else None

class ServicioRegistroDescargaApp(Servicio):

    def __init__(self, manejador_registrar_descarga: RegistrarDescargaHandler,
                 manejador_obtener_historial: ManejadorObtenerHistorial):
        self.manejador_registrar_descarga = manejador_registrar_descarga
        self.manejador_obtener_historial = manejador_obtener_historial

    def registrar_descarga(self, registro_descarga: RegistroDescargaDTO):
        comando = RegistrarDescarga(registro_descarga=registro_descarga)
        self.manejador_registrar_descarga.handle(comando)

    def obtener_historial_descargas(self, id_entrega: uuid.UUID) -> HistorialEntregaDTO:
        query = QueryObtenerHistorial(id_entrega=id_entrega)
        resultado = self.manejador_obtener_historial.handle(query)
        return resultado.historial if resultado else None
