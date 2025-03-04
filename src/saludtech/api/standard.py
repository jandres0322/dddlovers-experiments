import json
from flask import Response, request

import saludtech.seedwork.presentacion.api as api
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando

from saludtech.modulos.standard.aplicacion.mapeadores import MapeadorSolicitudDescargaDTOJson
from saludtech.modulos.standard.aplicacion.servicios import ServicioSolicitudDescarga
from saludtech.modulos.standard.aplicacion.comandos.solicitar_descarga import ComandoSolicitarDescarga

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


@bp.route('/solicitud-descarga-async', methods=('POST',))
def solicitar_descarga_async():
  try:
    solicitud_descarga_dict = request.json
    
    map_solicitud_descarga = MapeadorSolicitudDescargaDTOJson()
    solicitud_descarga_dto = map_solicitud_descarga.externo_a_dto(solicitud_descarga_dict)
    
    comando = ComandoSolicitarDescarga(
      fecha_actualizacion=solicitud_descarga_dto.fecha_actualizacion,
      fecha_creacion=solicitud_descarga_dto.fecha_creacion,
      imagenes=solicitud_descarga_dto.imagenes,
      usuario_id=solicitud_descarga_dto.usuario_id,
      id=solicitud_descarga_dto.id
    )
    
    ejecutar_commando(comando)
    
    return Response('{}', status=202, mimetype='application/json')    
  except ExcepcionDominio as e:
    return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')