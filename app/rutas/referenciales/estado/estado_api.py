from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.estado.estadoDao import EstadoDao

estadoapi = Blueprint('estadoapi', __name__)

# Trae todas las estados
@estadoapi.route('/estados', methods=['GET'])
def getEstados():
    estadodao = EstadoDao()

    try:
        estados = estadodao.getEstados()

        return jsonify({
            'success': True,
            'data': estados,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las estados: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estadoapi.route('/estados/<int:estado_id>', methods=['GET'])
def getEstado(estado_id):
    estadodao = EstadoDao()

    try:
        estado = estadodao.getEstadoById(estado_id)

        if estado:
            return jsonify({
                'success': True,
                'data': estado,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la estado con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener estado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva estado
@estadoapi.route('/estados', methods=['POST'])
def addEstado():
    data = request.get_json()
    estadodao = EstadoDao()

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
        estado_id = estadodao.guardarEstado(descripcion)
        if estado_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': estado_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la estado. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar estado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estadoapi.route('/estados/<int:estado_id>', methods=['PUT'])
def updateEstado(estado_id):
    data = request.get_json()
    estadodao = EstadoDao()

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
        if estadodao.updateEstado(estado_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': estado_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la estado con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar estado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estadoapi.route('/estados/<int:estado_id>', methods=['DELETE'])
def deleteEstado(estado_id):
    estadodao = EstadoDao()

    try:
        # Usar el retorno de eliminarEstado para determinar el éxito
        if estadodao.deleteEstado(estado_id):
            return jsonify({
                'success': True,
                'mensaje': f'Estado con ID {estado_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la estado con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar estado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500