from datetime import datetime
from .entidades import ImagenMedica
from .objetos_valor import EstadoImagen, EstadosImagen, MetadatosImagen

class FabricaImagen:
  @staticmethod
  def crear_objeto(id: str, nombre: str, formato: str, tamano_mb: float, resolucion: str, origen: str, fecha_captura: str, tipo_estudio: str) -> ImagenMedica:
    metadatos = MetadatosImagen(tamano_mb, resolucion, origen, fecha_captura, tipo_estudio)
    return ImagenMedica(
      id=id,
      nombre_archivo=nombre,
      formato=formato,
      fecha_creacion=datetime.utcnow(),
      estado=EstadoImagen(EstadosImagen.PENDIENTE),
      metadatos=metadatos
    )
