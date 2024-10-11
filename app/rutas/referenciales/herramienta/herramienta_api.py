from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.herramienta.herramientaDao import HerramientaDao

herramientaapi = Blueprint('herramientaapi', __name__)

# Trae todas las herramientas
@herramientaapi.route('/herramientas', methods=['GET'])
def getHerramientas():
    herramientadao = HerramientaDao()

    try:
        herramientas = herramientadao.getHerramientas()

        return jsonify({
            'success': True,
            'data': herramientas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las herramientas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@herramientaapi.route('/herramientas/<int:herramienta_id>', methods=['GET'])
def getHerramienta(herramienta_id):
    herramientadao = HerramientaDao()

    try:
        herramienta = herramientadao.getHerramientaById(herramienta_id)

        if herramienta:
            return jsonify({
                'success': True,
                'data': herramienta,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la herramienta con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener herramienta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva herramienta
@herramientaapi.route('/herramientas', methods=['POST'])
def addHerramienta():
    data = request.get_json()
    herramientadao = HerramientaDao()

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
        herramienta_id = herramientadao.guardarHerramienta(descripcion)
        if herramienta_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': herramienta_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la herramienta. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar herramienta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@herramientaapi.route('/herramientas/<int:herramienta_id>', methods=['PUT'])
def updateHerramienta(herramienta_id):
    data = request.get_json()
    herramientadao = HerramientaDao()

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
        if herramientadao.updateHerramienta(herramienta_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': herramienta_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la herramienta con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar herramienta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@herramientaapi.route('/herramientas/<int:herramienta_id>', methods=['DELETE'])
def deleteHerramienta(herramienta_id):
    herramientadao = HerramientaDao()

    try:
        # Usar el retorno de eliminarHerramienta para determinar el éxito
        if herramientadao.deleteHerramienta(herramienta_id):
            return jsonify({
                'success': True,
                'mensaje': f'Herramienta con ID {herramienta_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la herramienta con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar herramienta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500