from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modules.procesamiento_imagenes.dominio.entidades import ImagenProcesada


class MapeadorImagenMedica(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self):
        return ImagenProcesada.__class__
    
    def entidad_a_dto(self, entidad):
        return super().entidad_a_dto(entidad)
    
    def dto_a_entidad(self, dto):
        return super().dto_a_entidad(dto)
