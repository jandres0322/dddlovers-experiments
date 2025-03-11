from src.saludtech.modulos.usuarios.dominio.entidades import Usuario
from src.saludtech.modulos.usuarios.dominio.repositorios import UsuarioRepositorio

class EliminarUsuario:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def ejecutar(self, usuario_id: int) -> None:
        self.repositorio.eliminar(usuario_id)
