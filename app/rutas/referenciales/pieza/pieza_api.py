from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.pieza.PiezaDao import PiezaDao

piezaapi = Blueprint('piezaapi', __name__)

# Trae todas las piezas
@piezaapi.route('/piezas', methods=['GET'])
def getPiezas():
    piezadao = PiezaDao()

    try:
        piezas = piezadao.getPiezas()

        return jsonify({
            'success': True,
            'data': piezas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las piezas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@piezaapi.route('/piezas/<int:pieza_id>', methods=['GET'])
def getPieza(pieza_id):
    piezadao = PiezaDao()

    try:
        pieza = piezadao.getPiezaById(pieza_id)

        if pieza:
            return jsonify({
                'success': True,
                'data': pieza,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la pieza con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener pieza: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva pieza
@piezaapi.route('/piezas', methods=['POST'])
def addPieza():
    data = request.get_json()
    piezadao = PiezaDao()

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
        pieza_id = piezadao.guardarPieza(descripcion)
        if pieza_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': pieza_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la pieza. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar pieza: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@piezaapi.route('/piezas/<int:pieza_id>', methods=['PUT'])
def updatePieza(pieza_id):
    data = request.get_json()
    piezadao = PiezaDao()

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
        if piezadao.updatePieza(pieza_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': pieza_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la pieza con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar pieza: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@piezaapi.route('/piezas/<int:pieza_id>', methods=['DELETE'])
def deletePieza(pieza_id):
    piezadao = PiezaDao()

    try:
        # Usar el retorno de eliminarPieza para determinar el éxito
        if piezadao.deletePieza(pieza_id):
            return jsonify({
                'success': True,
                'mensaje': f'Pieza con ID {pieza_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la pieza con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar pieza: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500