from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from .entidades import SolicitudDescarga
from .reglas import ValidarFormatoDescarga, ValidarListaImagenes
from dataclasses import dataclass


@dataclass
class _FabricaSolicitudDescarga(Fabrica):
    def crear_objeto(self, obj, mapeador = None):
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            solicitud: SolicitudDescarga = mapeador.dto_a_entidad(obj)
                        
            self.validar_regla(ValidarFormatoDescarga(solicitud.formato.value))
            self.validar_regla(ValidarListaImagenes(solicitud.imagenes))
                        
            return solicitud
        
@dataclass
class FabricaSolicitudDescarga(Fabrica):
    
    def crear_objeto(self, obj, mapeador = None):
        if mapeador.obtener_tipo() == SolicitudDescarga.__class__:
            fabrica_solicitud = _FabricaSolicitudDescarga()
            return fabrica_solicitud.crear_objeto(obj, mapeador)
