from flask import json, jsonify

def bad_request(details_error="We don't have datails"):
    return jsonify(
        {
            'success': False,
            'data': {},
            'messages': 'Bad request',
            'code': 400,
            'details_error': details_error,
        }
    ), 400

def not_found():
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Resource not found',
            'code': 404
        }
    ), 404

def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200