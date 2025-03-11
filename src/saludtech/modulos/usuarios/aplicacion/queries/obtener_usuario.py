from src.saludtech.modulos.usuarios.dominio.entidades import Usuario
from src.saludtech.modulos.usuarios.dominio.repositorios import UsuarioRepositorio

class ObtenerUsuario:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def ejecutar(self, usuario_id: int) -> Usuario:
        return self.repositorio.obtener_por_id(usuario_id)
    
class ObtenerUsuarios:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def ejecutar(self) -> Usuario:
        return self.repositorio.obtener_todos()