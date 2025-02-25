from seedwork.aplicacion.queries import Query, QueryResultado, QueryHandler
from saludtech.modulos.imagenes.dominio.repositorios import RepositorioEntregaImagen
from saludtech.modulos.imagenes.aplicacion.dto import EntregaImagenDTO
from saludtech.modulos.imagenes.aplicacion.mapeadores import MapeadorEntregaImagen
import uuid
from dataclasses import dataclass

@dataclass
class QueryObtenerEntrega(Query):
    id_entrega: uuid.UUID

@dataclass
class ResultadoEntrega(QueryResultado):
    entrega: EntregaImagenDTO

class ManejadorObtenerEntrega(QueryHandler):

    def __init__(self, repositorio: RepositorioEntregaImagen, mapeador: MapeadorEntregaImagen):
        self.repositorio = repositorio
        self.mapeador = mapeador

    def handle(self, query: QueryObtenerEntrega) -> ResultadoEntrega:
        entrega = self.repositorio.obtener_por_id(query.id_entrega)
        if not entrega:
            return None
        
        entrega_dto = self.mapeador.externo_a_dto(entrega)
        return ResultadoEntrega(entrega=entrega_dto)
