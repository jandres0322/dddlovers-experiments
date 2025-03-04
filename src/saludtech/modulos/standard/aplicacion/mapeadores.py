
from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap

from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga, ImagenMedica

from .dto import SolicitudDescargaDTO, ImagenMedicaDTO

class MapeadorSolicitudDescargaDTOJson(AppMap):
  
  def _procesar_imagenes_medicas(self, imagen: dict) -> ImagenMedicaDTO:
    return ImagenMedicaDTO(
      id=imagen.get('imagen_id'),
      imagen_id=imagen.get('imagen_id'),
      formato=imagen.get('formato'),
    )

  def externo_a_dto(self, externo:dict) -> SolicitudDescargaDTO:
    solicitud_descarga_dto = SolicitudDescargaDTO(
      usuario_id=externo.get('usuario_id'),
    )
    
    for imagen in externo.get('imagenes'):
      solicitud_descarga_dto.imagenes.append(self._procesar_imagenes_medicas(imagen))
    
    return solicitud_descarga_dto
    
  
  def dto_a_externo(self, dto):
    return dto.__dict__


class MapeadorSolicitudDescarga(RepMap):  
  _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

  
  def obtener_tipo(self):
    return SolicitudDescarga.__class__
  
  def dto_a_entidad(self, dto: SolicitudDescargaDTO) -> SolicitudDescarga:
    
    solicitud_descarga = SolicitudDescarga()
    solicitud_descarga.id_usuario = dto.usuario_id
    solicitud_descarga.imagenes = list()
    
    imagenes_dto: list[ImagenMedicaDTO] = dto.imagenes
    
    for imagen_dto in imagenes_dto:
      imagen = ImagenMedica(
        formato=imagen_dto.formato
      )
      solicitud_descarga.imagenes.append(imagen)
    
    return solicitud_descarga
  
  def entidad_a_dto(self, entidad: SolicitudDescarga) -> SolicitudDescargaDTO:
    fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
    fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
    _id = str(entidad.id)
    imagenes_medicas = list()
    
    for imagen in entidad.imagenes:
      imagenes_medicas.append(ImagenMedicaDTO(
        id=imagen.id,
        formato=imagen.formato
      ))
          
    return SolicitudDescargaDTO(
      fecha_creacion=fecha_creacion,
      fecha_actualizacion=fecha_actualizacion,
      id=_id,
      usuario_id=entidad.id_usuario,
      imagenes=imagenes_medicas
    )