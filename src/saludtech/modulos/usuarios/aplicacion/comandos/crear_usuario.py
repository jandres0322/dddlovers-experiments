from src.saludtech.modulos.usuarios.dominio.entidades import Usuario
from src.saludtech.modulos.usuarios.dominio.repositorios import UsuarioRepositorio

class CrearUsuario:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def ejecutar(self, datos_usuario: dict) -> Usuario:
        usuario = Usuario(**datos_usuario)
        return self.repositorio.guardar(usuario)