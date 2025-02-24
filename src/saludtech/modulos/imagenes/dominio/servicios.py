from datetime import datetime
from .repositorios import RepositorioImagenes
from .objetos_valor import EstadoImagen, EstadosImagen
from .eventos import ImagenProcesada
from .excepciones import ImagenNoEncontradaError

class ServicioProcesamientoImagen:
  def __init__(self, repositorio: RepositorioImagenes):
    self.repositorio = repositorio

  def procesar_imagen(self, id_imagen: str):
    imagen = self.repositorio.obtener_por_id(id_imagen)
    if not imagen:
      raise ImagenNoEncontradaError(id_imagen)
    
    imagen.estado = EstadoImagen(EstadosImagen.PROCESADA)
    self.repositorio.guardar(imagen)
    
    return ImagenProcesada(
      id_imagen=imagen.id,
      fecha_procesamiento=datetime.utcnow()
    )
