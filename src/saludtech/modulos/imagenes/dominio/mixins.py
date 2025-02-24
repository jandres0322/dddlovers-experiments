import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from seedwork.dominio.excepciones import ReglaNegocioExcepcion

class FormatoMixin:
    """Mixin para validaciones de formato de imagen."""
    
    FORMATOS_PERMITIDOS = {f.value for f in ov.FormatosPermitidos}

    def validar_formato(self, formato: str):
        """Valida que el formato de la imagen esté permitido."""
        if formato.lower() not in self.FORMATOS_PERMITIDOS:
            raise ReglaNegocioExcepcion(f"Formato '{formato}' no permitido. Formatos válidos: {self.FORMATOS_PERMITIDOS}")

class EstadoMixin:
    """Mixin para gestionar los estados de una imagen médica."""

    def cambiar_estado(self, nuevo_estado: ov.EstadoImagen):
        """Cambia el estado de la imagen validando que sea un estado permitido."""
        if nuevo_estado not in ov.EstadoImagen:
            raise ReglaNegocioExcepcion(f"Estado '{nuevo_estado}' no permitido. Estados válidos: {list(ov.EstadoImagen)}")
        self.estado = nuevo_estado
