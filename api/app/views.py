from flask import jsonify
from flask import Blueprint
from flask.blueprints import BlueprintSetupState

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({
        'message': 'Hola, desde el endpoint listado de tareas.'
    })

@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task():
    pass

@api_v1.route('/tasks/', methods=['POST'])
def create_task():
    pass

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass

@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task():
    pass