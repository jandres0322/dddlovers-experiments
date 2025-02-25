from seedwork.dominio.reglas import ReglaNegocio
import saludtech.modulos.imagenes.dominio.objetos_valor as ov

class ReglaEntregaDisponible(ReglaNegocio):

    def __init__(self, estado: ov.EstadoEntrega, mensaje="La imagen aún no está disponible para entrega."):
        super().__init__(mensaje)
        self.estado = estado

    def es_valido(self) -> bool:
        return self.estado == ov.EstadoEntrega.DISPONIBLE

class ReglaRegistroDescarga(ReglaNegocio):

    def __init__(self, historial_descargas: list, mensaje="El historial de descargas no puede estar vacío."):
        super().__init__(mensaje)
        self.historial_descargas = historial_descargas

    def es_valido(self) -> bool:
        return len(self.historial_descargas) > 0

