from saludtech.seedwork.aplicacion.dto import Mapeador as AppMapper
from .dto import ObtenerImagenesDTO

class MapeadorObtenerImagenesDTOJson(AppMapper):
    
    def externo_a_dto(self, externo: dict) -> ObtenerImagenesDTO:
        
        obtener_imagenes_dto = ObtenerImagenesDTO(
            id_solicitud=externo['id_solicitud'],
            id_imagenes=externo['id_imagenes'].split(',')
        )
        return obtener_imagenes_dto
    
    def dto_a_externo(self, dto):
        return super().dto_a_externo(dto)