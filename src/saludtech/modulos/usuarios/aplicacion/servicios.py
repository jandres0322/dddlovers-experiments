from saludtech.modulos.usuarios.aplicacion.dto import UsuarioDTO
from saludtech.modulos.usuarios.aplicacion.mapeadores import UsuarioMapeador
from saludtech.modulos.usuarios.infraestructura.repositorios import RepositorioUsuarioSQL
from saludtech.modulos.usuarios.dominio.entidades import Usuario

class UsuarioServicio:
    def __init__(self, repositorio: RepositorioUsuarioSQL):
        self.repositorio = repositorio

    def crear_usuario(self, dto: UsuarioDTO) -> UsuarioDTO:
        usuario = UsuarioMapeador.dto_a_externo(dto=dto)
        usuario_creado = self.repositorio.agregar(usuario)
        return UsuarioMapeador.externo_a_dto(usuario_creado)

    def obtener_usuario(self, usuario_id: int) -> UsuarioDTO:
        usuario = self.repositorio.obtener_por_id(usuario_id)
        return UsuarioMapeador.externo_a_dto(usuario) if usuario else None
    
    def obtener_usuarios(self):
        usuario = self.repositorio.obtener_todos()
        return usuario

    def actualizar_usuario(self, usuario_id: int, dto: UsuarioDTO) -> UsuarioDTO:
        usuario_existente = self.repositorio.obtener_por_id(usuario_id)
        if not usuario_existente:
            raise ValueError("Usuario no encontrado")
        
        usuario_existente.nombre = dto.nombre
        usuario_existente.email = dto.email
        
        usuario_actualizado = self.repositorio.guardar(usuario_existente)
        return UsuarioMapeador.externo_a_dto(usuario_actualizado)
