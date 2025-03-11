import uuid
import saludtech.seedwork.presentacion.api as api
from saludtech.modulos.usuarios.aplicacion.servicios import UsuarioServicio
from saludtech.modulos.usuarios.aplicacion.mapeadores import UsuarioMapeador
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.usuarios.aplicacion.servicios import UsuarioServicio
from saludtech.modulos.usuarios.infraestructura.repositorios import RepositorioUsuarioSQL
from saludtech.modulos.usuarios.aplicacion.dto import UsuarioDTO

bp = api.crear_blueprint('users', '/usuarios')

@bp.route('/<int:string>', methods=['GET'])
def obtener_usuario(id=None):
  if id:
    repositorio = RepositorioUsuarioSQL()
    map_entrega = UsuarioMapeador()
    servicio_dominio = UsuarioServicio(repositorio=repositorio)
    usuario = servicio_dominio.obtener_usuario(id)
    return map_entrega.dto_a_externo(usuario).__dict__
  else:
    raise ExcepcionDominio('Id del usuario no especificado')
  
@bp.route('/', methods=['POST'])
def crear_usuario():
  repositorio = RepositorioUsuarioSQL()
  map_entrega = UsuarioMapeador()
  id = uuid.uuid4()
  usuario_dto = UsuarioDTO(id, "Diego", f"prueba-1@gmail.com")
  servicio_dominio = UsuarioServicio(repositorio=repositorio)
  usuario = servicio_dominio.crear_usuario(usuario_dto)
  return map_entrega.dto_a_externo(usuario).__dict__
    