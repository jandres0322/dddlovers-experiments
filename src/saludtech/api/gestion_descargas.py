from flask import request, Response

from saludtech.seedwork.presentacion import api
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.modules.gestion_descargas.aplicacion.mapeadores import MapeadorSolicitudDTOJson
from saludtech.modules.gestion_descargas.aplicacion.comandos.solicitar_descargar import ComandoSolicitarDescarga


bp = api.crear_blueprint('gestion-descargas', '/gestion-descargas')

@bp.route('/solicitar', methods=('POST',))
def solicitar_descarga():
    try:
        
        solicitud_dict = request.json
        
        map_solicitud = MapeadorSolicitudDTOJson()
        solicitud_dto = map_solicitud.externo_a_dto(solicitud_dict)
                        
        comando = ComandoSolicitarDescarga(
            id_usuario=solicitud_dto.id_usuario,
            imagenes=solicitud_dto.imagenes,
            formato=solicitud_dto.formato,
            estado=solicitud_dto.estado
        )
                
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response('{}', status=500, mimetype='application/json')