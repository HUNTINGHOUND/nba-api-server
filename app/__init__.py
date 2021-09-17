from flask_api import FlaskAPI
from instance.config import app_config
from flask import request, jsonify, abort


def create_app(config_name):
    from app.model import GetInfo

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/playerinfo', methods=['GET'])
    def get_player_info():
        player_id = request.args.get('playerid', '')
        data = GetInfo.getPlayerInfo(player_id)

        response = jsonify(data)
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    @app.route('/shotchart', methods=['GET'])
    def get_shot_data():
        player_id = request.args.get('playerid', '')
        data = GetInfo.getShot(player_id, 0)

        response = jsonify(data)
        response.status_code = 200
        response.headers['Acess-Control-Allow-Origin'] = '*'
        return response

    return app
