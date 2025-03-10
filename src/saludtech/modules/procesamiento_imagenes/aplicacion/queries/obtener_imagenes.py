from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado, ejecutar_query as query

class ObtenerImagenes(Query):
    id_solicitud: str
    
    
class ObtenerImagenesHandler(QueryHandler):
    def __init__(self):
        ...
    
    def handle(self, query: ObtenerImagenes):
        ...
        
        
@query.register(ObtenerImagenes)
def ejecutar_query_obtener_imagenes(query: ObtenerImagenes):
    handler = ObtenerImagenesHandler()
    return handler.handle(query)