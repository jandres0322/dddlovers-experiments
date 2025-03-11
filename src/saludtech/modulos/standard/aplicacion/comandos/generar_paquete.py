
from saludtech.modulos.standard.aplicacion.dto import ImagenMedicaDTO
from saludtech.seedwork.aplicacion.comandos import Comando


class ComandoGenerarPaquete(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    usuario_id: str
    imagenes: list[ImagenMedicaDTO]

class ComandoRevertirPaquete(Comando):
    ...
