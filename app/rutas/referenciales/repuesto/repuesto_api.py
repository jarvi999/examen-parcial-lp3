from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.repuesto.RepuestoDao import RepuestoDao

repuestoapi = Blueprint('repuestoapi', __name__)

# Trae todas las repuestos
@repuestoapi.route('/repuestos', methods=['GET'])
def getRepuestos():
    repuestodao = RepuestoDao()

    try:
        repuestos = repuestodao.getRepuestos()

        return jsonify({
            'success': True,
            'data': repuestos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las repuestos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@repuestoapi.route('/repuestos/<int:repuesto_id>', methods=['GET'])
def getRepuesto(repuesto_id):
    repuestodao = RepuestoDao()

    try:
        repuesto = repuestodao.getRepuestoById(repuesto_id)

        if repuesto:
            return jsonify({
                'success': True,
                'data': repuesto,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la repuesto con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener repuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva repuesto
@repuestoapi.route('/repuestos', methods=['POST'])
def addRepuesto():
    data = request.get_json()
    repuestodao = RepuestoDao()

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
        repuesto_id = repuestodao.guardarRepuesto(descripcion)
        if repuesto_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': repuesto_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la repuesto. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar repuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@repuestoapi.route('/repuestos/<int:repuesto_id>', methods=['PUT'])
def updateRepuesto(repuesto_id):
    data = request.get_json()
    repuestodao = RepuestoDao()

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
        if repuestodao.updateRepuesto(repuesto_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': repuesto_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la repuesto con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar repuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@repuestoapi.route('/repuestos/<int:repuesto_id>', methods=['DELETE'])
def deleteRepuesto(repuesto_id):
    repuestodao = RepuestoDao()

    try:
        # Usar el retorno de eliminarRepuesto para determinar el éxito
        if repuestodao.deleteRepuesto(repuesto_id):
            return jsonify({
                'success': True,
                'mensaje': f'Repuesto con ID {repuesto_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la repuesto con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar repuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500