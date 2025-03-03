from saludtech.seedwork.aplicacion.queries import Query, QueryResultado, QueryHandler
from saludtech.modulos.imagenes.dominio.repositorios import RepositorioHistorialEntrega
from saludtech.modulos.imagenes.aplicacion.dto import HistorialEntregaDTO
from saludtech.modulos.imagenes.aplicacion.dto import MapeadorHistorialEntrega
import uuid
from dataclasses import dataclass

@dataclass
class QueryObtenerHistorial(Query):
    """Query para obtener el historial de descargas de una imagen procesada."""
    id_entrega: uuid.UUID

@dataclass
class ResultadoHistorial(QueryResultado):
    """Resultado de la consulta del historial de descargas de una imagen procesada."""
    historial: HistorialEntregaDTO  # Ahora usa un DTO en lugar de atributos separados

class ManejadorObtenerHistorial(QueryHandler):
    """Manejador del query para obtener el historial de descargas de una imagen procesada."""

    def __init__(self, repositorio: RepositorioHistorialEntrega, mapeador: MapeadorHistorialEntrega):
        self.repositorio = repositorio
        self.mapeador = mapeador

    def handle(self, query: QueryObtenerHistorial) -> ResultadoHistorial:
        """Ejecuta la consulta del historial de descargas."""
        historial = self.repositorio.obtener_por_id(query.id_entrega)
        if not historial:
            return None
        
        historial_dto = self.mapeador.externo_a_dto(historial)
        return ResultadoHistorial(historial=historial_dto)
