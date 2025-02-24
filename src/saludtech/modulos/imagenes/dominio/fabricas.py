from datetime import datetime
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from saludtech.modulos.imagenes.dominio.entidades import ImagenMedica
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.excepciones import ReglaNegocioExcepcion

class FabricaImagenes(Fabrica):

    @staticmethod
    def crear_objeto(id: str, nombre_archivo: str, formato: str, fecha_creacion: datetime,
                     tamano_mb: float, resolucion: str, origen: str, fecha_captura: str, tipo_estudio: str) -> ImagenMedica:

        if formato.lower() not in {f.value for f in ov.FormatosPermitidos}:
            raise ReglaNegocioExcepcion(f"Formato de imagen '{formato}' no permitido. Formatos válidos: {list(ov.FormatosPermitidos)}")

        # Crear objeto de valor MetadatosImagen
        metadatos = ov.MetadatosImagen(
            tamano_mb=tamano_mb,
            resolucion=resolucion,
            origen=origen,
            fecha_captura=fecha_captura,
            tipo_estudio=tipo_estudio
        )

        # Retornar la entidad creada
        return ImagenMedica(
            id=id,
            nombre_archivo=nombre_archivo,
            formato=formato,
            fecha_creacion=fecha_creacion,
            estado=ov.EstadoImagen.PENDIENTE,
            metadatos=metadatos,
            url=""
        )
