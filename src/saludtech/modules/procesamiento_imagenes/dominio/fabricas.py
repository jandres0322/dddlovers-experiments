from dataclasses import dataclass
from .entidades import ImagenProcesada
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad

@dataclass
class _FabricaImagenProesada(Fabrica):
	def crear_objeto(self, obj, mapeador = None):
		if isinstance(obj, Entidad):
			return mapeador.entidad_a_dto(obj)
		else:
			imagen: ImagenProcesada = mapeador.dto_a_entidad(obj)

				## Aqui van las reglas de dominio

			return imagen
    
@dataclass
class FabricaImagenProcesada(Fabrica):
	def crear_objeto(self, obj, mapeador = None):
		if mapeador.obtener_tipo() == ImagenProcesada.__class__:
			fabrica_obtener_imagen = _FabricaImagenProesada()
			return fabrica_obtener_imagen.crear_objeto(obj, mapeador)
