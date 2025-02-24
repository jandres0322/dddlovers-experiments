import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from seedwork.dominio.reglas import ReglaNegocio

class ReglaFormatoImagen(ReglaNegocio):

    def __init__(self, formato: str, mensaje="Formato de imagen no permitido"):
        super().__init__(mensaje)
        self.formato = formato

    def es_valido(self) -> bool:
        return self.formato.lower() in {f.value for f in ov.FormatosPermitidos}

class ReglaTamanioImagen(ReglaNegocio):

    TAMANIO_MAXIMO_MB = 50  # 50MB

    def __init__(self, tamano_mb: float, mensaje="El tamaño de la imagen excede el límite permitido"):
        super().__init__(mensaje)
        self.tamano_mb = tamano_mb

    def es_valido(self) -> bool:
        """Verifica que el tamaño de la imagen no exceda el límite."""
        return self.tamano_mb <= self.TAMANIO_MAXIMO_MB

class ReglaCambioEstado(ReglaNegocio):

    def __init__(self, estado_actual: ov.EstadoImagen, nuevo_estado: ov.EstadoImagen,
                 mensaje="Cambio de estado no permitido"):
        super().__init__(mensaje)
        self.estado_actual = estado_actual
        self.nuevo_estado = nuevo_estado

    def es_valido(self) -> bool:
        estados_validos = {
            ov.EstadoImagen.PENDIENTE: [ov.EstadoImagen.PROCESADA, ov.EstadoImagen.ERROR],
            ov.EstadoImagen.PROCESADA: [],
            ov.EstadoImagen.ERROR: []
        }
        return self.nuevo_estado in estados_validos[self.estado_actual]
