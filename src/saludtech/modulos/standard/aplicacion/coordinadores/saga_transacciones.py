
from saludtech.modules.gestion_descargas.dominio.repositorios import RepositorioSolicitudDescarga
from saludtech.modulos.standard.aplicacion.comandos.cancelar_descarga import CancelarDescarga
from saludtech.modulos.standard.aplicacion.comandos.generar_paquete import ComandoGenerarPaquete, ComandoRevertirPaquete
from saludtech.modulos.standard.aplicacion.comandos.notificar_usuario import ComandoNotificarUsuario
from saludtech.modulos.standard.aplicacion.comandos.solicitar_descarga import ComandoSolicitarDescarga
from saludtech.modulos.standard.dominio.eventos import GenerarPaqueteFallido, NotificacionGenerada, NotificarUsuarioFallido, PaqueteGenerado, SolicitudDescargaCreada, SolicitudDescargaFallida
from saludtech.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Inicio, Transaccion
from saludtech.seedwork.dominio.eventos import EventoDominio


class CoordinadorTransacciones(CoordinadorOrquestacion):
    
    def inicializar_pasos(self):
        self.pasos = [
            Inicio(),
            Transaccion(index=1, comando=ComandoSolicitarDescarga, evento=SolicitudDescargaCreada, error=SolicitudDescargaFallida, compensacion=CancelarDescarga),
            Transaccion(index=2, comando=ComandoGenerarPaquete, evento=PaqueteGenerado , error= GenerarPaqueteFallido, compensacion=ComandoRevertirPaquete),
            Transaccion(index=3, comando=ComandoNotificarUsuario, evento=NotificacionGenerada , error=NotificarUsuarioFallido, compensacion=ComandoRevertirPaquete)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        RepositorioSolicitudDescarga().agregar_log(mensaje)

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        if isinstance(evento, SolicitudDescargaCreada) and not isinstance(tipo_comando, ComandoGenerarPaquete):
            ComandoGenerarPaquete()
        elif isinstance(evento, PaqueteGenerado) and not isinstance(tipo_comando, ComandoNotificarUsuario):
            ComandoNotificarUsuario()