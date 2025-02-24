from uuid import UUID
from datetime import datetime
from seedwork.dominio.servicios import Servicio
from saludtech.modulos.imagenes.dominio.entidades import ImagenMedica
from saludtech.modulos.imagenes.dominio.objetos_valor import EstadoImagen, MetadatosImagen
from saludtech.modulos.imagenes.dominio.repositorios import RepositorioImagenes
from saludtech.modulos.imagenes.dominio.reglas import ReglaFormatoImagen, ReglaTamanioImagen, ReglaCambioEstado

class ServicioImagenes(Servicio):

    def __init__(self, repositorio: RepositorioImagenes):
        self.repositorio = repositorio

    def subir_imagen(self, id: str, nombre_archivo: str, formato: str, tamano_mb: float, resolucion: str,
                     origen: str, fecha_captura: str, tipo_estudio: str) -> ImagenMedica:

        self.validar_reglas([
            ReglaFormatoImagen(formato),
            ReglaTamanioImagen(tamano_mb)
        ])

        metadatos = MetadatosImagen(
            tamano_mb=tamano_mb,
            resolucion=resolucion,
            origen=origen,
            fecha_captura=fecha_captura,
            tipo_estudio=tipo_estudio
        )

        imagen = ImagenMedica(
            id=id,
            nombre_archivo=nombre_archivo,
            formato=formato,
            fecha_creacion=datetime.utcnow(),
            estado=EstadoImagen.PENDIENTE,
            metadatos=metadatos,
            url=""
        )

        self.repositorio.agregar(imagen)
        return imagen

    def procesar_imagen(self, id: UUID, url_procesada: str):
        imagen = self.repositorio.obtener_por_id(id)
        if not imagen:
            raise ValueError(f"No se encontró la imagen con ID {id}")

        self.validar_reglas([ReglaCambioEstado(imagen.estado, EstadoImagen.PROCESADA)])

        imagen.marcar_como_procesada(url_procesada)
        self.repositorio.actualizar(imagen)
        return imagen
