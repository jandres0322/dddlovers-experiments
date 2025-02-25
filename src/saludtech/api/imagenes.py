import saludtech.seedwork.presentacion.api as api
from saludtech.modulos.imagenes.aplicacion.servicios import ServicioEntregaImagenApp
from saludtech.modulos.imagenes.aplicacion.mapeadores import MapeadorEntregaImagen
from saludtech.modulos.imagenes.aplicacion.mapeadores import MapeadorHistorialEntrega
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.imagenes.aplicacion.comandos.marcar_disponible import MarcarDisponibleHandler
from saludtech.modulos.imagenes.aplicacion.comandos.registrar_descarga import RegistrarDescargaHandler
from saludtech.modulos.imagenes.aplicacion.queries.obtener_entrega import ManejadorObtenerEntrega
from saludtech.modulos.imagenes.dominio.servicios import ServicioEntregaImagen
from saludtech.modulos.imagenes.infraestructura.repositorios import RepositorioEntregaImagenSQLAlchemy

bp = api.crear_blueprint('imagen', '/imagen')

@bp.route('/<id>', methods=['GET'])
def obtener_imagen(id=None):
  if id:
    repositorio = RepositorioEntregaImagenSQLAlchemy()
    map_entrega = MapeadorEntregaImagen()
    servicio_dominio = ServicioEntregaImagen(repositorio_entrega=repositorio)
    manejador_entrega = MarcarDisponibleHandler(servicio=servicio_dominio, mapeador=map_entrega)
    manejador_registrar_descargar = ManejadorObtenerEntrega(mapeador=map_entrega, repositorio=repositorio)
    sr = ServicioEntregaImagenApp(manejador_marcar_disponible=manejador_entrega, manejador_obtener_entrega=manejador_registrar_descargar)
    return map_entrega.dto_a_externo(sr.obtener_entrega(id))    
  else:
    raise ExcepcionDominio('Id de imagen no especificado')
    