from dataclasses import dataclass
from datetime import datetime
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from seedwork.dominio.entidades import Entidad


@dataclass
class ImagenMedica(Entidad):
    id: str
    nombre_archivo: str
    formato: str
    fecha_creacion: datetime
    estado: ov.EstadoImagen.PENDIENTE
    metadatos: ov.MetadatosImagen
    url: str

    def marcar_como_procesada(self, url: str):
        self.estado = ov.EstadoImagen.PROCESADA
        self.url = url
        
    def validar_formato(self):
        if self.formato not in ov.FormatosPermitidos:
            raise ValueError(f"Formato de imagen no soportado: {self.formato}")

