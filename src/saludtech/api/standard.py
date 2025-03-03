import json
from flask import Response, request

import saludtech.seedwork.presentacion.api as api
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio

from saludtech.modulos.standard.aplicacion.mapeadores import MapeadorSolicitudDescargaDTOJson
from saludtech.modulos.standard.aplicacion.servicios import ServicioSolicitudDescarga

bp = api.crear_blueprint('standard', '/standard')

@bp.route('/solicitud-descarga', methods=('POST',))
def solicitar_descarga():
  try:
    solicitud_descarga_dict = request.json
    
    map_solicitud_descarga = MapeadorSolicitudDescargaDTOJson()
    solicitud_descarga_dto = map_solicitud_descarga.externo_a_dto(solicitud_descarga_dict)

    servicio = ServicioSolicitudDescarga()
    
    dto_final = servicio.solicitar_descarga(solicitud_descarga_dto)
    
    return map_solicitud_descarga.dto_a_externo(dto_final)
    
  except ExcepcionDominio as e:
    return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
