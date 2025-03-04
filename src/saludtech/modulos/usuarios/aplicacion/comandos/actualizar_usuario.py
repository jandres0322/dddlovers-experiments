from src.saludtech.modulos.usuarios.dominio.entidades import Usuario
from src.saludtech.modulos.usuarios.dominio.repositorios import UsuarioRepositorio

class ActualizarUsuario:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def ejecutar(self, usuario_id: int, datos_actualizados: dict) -> Usuario:
        usuario = self.repositorio.obtener_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        
        for clave, valor in datos_actualizados.items():
            setattr(usuario, clave, valor)
        
        return self.repositorio.guardar(usuario)