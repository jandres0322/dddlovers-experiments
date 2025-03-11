from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado, ejecutar_query as query
from saludtech.modules.procesamiento_imagenes.dominio.fabricas import FabricaImagenProcesada
from saludtech.modules.procesamiento_imagenes.aplicacion.dto import ObtenerImagenesDTO
from saludtech.modules.procesamiento_imagenes.infraestructura.fabricas import FabricaRepositorio
from saludtech.modules.procesamiento_imagenes.dominio.repositorios import RepositorioImagenesProcesada
from saludtech.modules.procesamiento_imagenes.dominio.entidades import ImagenProcesada
from saludtech.modules.procesamiento_imagenes.aplicacion.mapeadores import MapeadorObtenerImagenes
from dataclasses import dataclass

@dataclass
class ObtenerImagenes(Query):
    id_solicitud: str
    id_imagenes: list[str]
    
    
class ObtenerImagenesHandler(QueryHandler):
    def __init__(self):
        self.fabrica_imagen = FabricaImagenProcesada()
        self.fabrica_repositorio = FabricaRepositorio()
    
    def handle(self, query: ObtenerImagenes):
        obtener_imagen_dto = ObtenerImagenesDTO(
            id_imagenes=query.id_imagenes,
            id_solicitud=query.id_solicitud
        )

        imagenes_medicas = []
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenesProcesada)
        for id_imagen in obtener_imagen_dto.id_imagenes:
            imagen: ImagenProcesada = repositorio.obtener_por_id(id_imagen)
            imagenes_medicas.append(self.fabrica_imagen.crear_objeto(imagen, MapeadorObtenerImagenes))
        
        print('imagenes_medicas', imagenes_medicas.__dict__)
        
        
@query.register(ObtenerImagenes)
def ejecutar_query_obtener_imagenes(query: ObtenerImagenes):
    handler = ObtenerImagenesHandler()
    return handler.handle(query)