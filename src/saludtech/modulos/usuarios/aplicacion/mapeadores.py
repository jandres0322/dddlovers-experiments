from saludtech.seedwork.aplicacion.dto import Mapeador
from saludtech.modulos.usuarios.infraestructura.dto import UsuarioORM
from saludtech.modulos.usuarios.aplicacion.dto import UsuarioDTO

class UsuarioMapeador(Mapeador):
    @staticmethod
    def externo_a_dto(usuario: UsuarioORM) -> UsuarioDTO:
        return UsuarioDTO(
            id=usuario.id,
            nombre=usuario.nombre,
            correo=usuario.correo,
        )
    @staticmethod
    def dto_a_externo(dto: UsuarioDTO) -> UsuarioORM:
        return UsuarioORM(
            id=dto.id,
            nombre=dto.nombre,
            correo=dto.correo,
        )