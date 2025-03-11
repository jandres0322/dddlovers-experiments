from saludtech.seedwork.aplicacion.dto import Mapeador as AppMapper
from saludtech.seedwork.dominio.repositorios import Mapeador as RepoMapper
from saludtech.modules.procesamiento_imagenes.dominio.entidades import ImagenProcesada
from .dto import ObtenerImagenesDTO, ImagenMedicaDTO
import ast

class MapeadorObtenerImagenesDTOJson(AppMapper):
    
    def externo_a_dto(self, externo: dict) -> ObtenerImagenesDTO:
        obtener_imagenes_dto = ObtenerImagenesDTO(
            id_solicitud=externo.id_solicitud,
            id_imagenes=ast.literal_eval(externo.id_imagenes)
        )
        return obtener_imagenes_dto
    
    def dto_a_externo(self, dto):
        return super().dto_a_externo(dto)
    
class MapeadorObtenerImagenes(RepoMapper):
    
    def obtener_tipo(self):
        return ImagenProcesada.__class__
    
    def entidad_a_dto(self, entidad: ImagenProcesada) -> ImagenMedicaDTO:
        _id = str(entidad.id)

        return ImagenMedicaDTO(
            _id,
            entidad.ruta_storage,
            entidad.ruta_thumbanil,
            entidad.ruta_metadatos
        )
    
    
    def dto_a_entidad(self, dto: ImagenMedicaDTO):
        imagen = ImagenProcesada()
        imagen.ruta_metadatos = dto.ruta_metadatos
        imagen.ruta_storage = dto.ruta_storage
        imagen.ruta_thumbanil = dto.ruta_thumbanil

        return imagen

