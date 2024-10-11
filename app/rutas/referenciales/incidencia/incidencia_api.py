from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.incidencia.IncidenciaDao import IncidenciaDao

incidenciaapi = Blueprint('incidenciaapi', __name__)

# Trae todas las incidencias
@incidenciaapi.route('/incidencias', methods=['GET'])
def getIncidencias():
    incidenciadao = IncidenciaDao()

    try:
        incidencias = incidenciadao.getIncidencias()

        return jsonify({
            'success': True,
            'data': incidencias,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las incidencias: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@incidenciaapi.route('/incidencias/<int:incidencia_id>', methods=['GET'])
def getIncidencia(incidencia_id):
    incidenciadao = IncidenciaDao()

    try:
        incidencia = incidenciadao.getIncidenciaById(incidencia_id)

        if incidencia:
            return jsonify({
                'success': True,
                'data': incidencia,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la incidencia con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener incidencia: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva incidencia
@incidenciaapi.route('/incidencias', methods=['POST'])
def addIncidencia():
    data = request.get_json()
    incidenciadao = IncidenciaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        descripcion = data['descripcion'].upper()
        incidencia_id = incidenciadao.guardarIncidencia(descripcion)
        if incidencia_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': incidencia_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la incidencia. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar incidencia: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@incidenciaapi.route('/incidencias/<int:incidencia_id>', methods=['PUT'])
def updateIncidencia(incidencia_id):
    data = request.get_json()
    incidenciadao = IncidenciaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    descripcion = data['descripcion']
    try:
        if incidenciadao.updateIncidencia(incidencia_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': incidencia_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la incidencia con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar incidencia: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@incidenciaapi.route('/incidencias/<int:incidencia_id>', methods=['DELETE'])
def deleteIncidencia(incidencia_id):
    incidenciadao = IncidenciaDao()

    try:
        # Usar el retorno de eliminarIncidencia para determinar el éxito
        if incidenciadao.deleteIncidencia(incidencia_id):
            return jsonify({
                'success': True,
                'mensaje': f'Incidencia con ID {incidencia_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la incidencia con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar incidencia: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500