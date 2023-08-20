from flask import (Blueprint, jsonify, current_app, request)
import pymysql
import datetime
from utils.db_ops import DBOps

# Flask Blueprint
post_method = Blueprint("post_method", __name__)


@post_method.route("/users/<user_id>/", methods=["POST"])
def post_route(user_id):
    """
    Insert user in the database
    """

    db_ops = DBOps()

    try:

        user_exist = db_ops.is_user_in_db(user_id)
        if user_exist:
            response = {"Status": "ERROR", "reason": "ID already exists"}
            return jsonify(response), f'code: {500}'

        data = request.get_json()
        user_name = data.get('user_name')

        db_ops.insert_user(user_id, user_name)

        response = {"Status": "OK", "User_added": f"{user_name}"}
        return jsonify(response), f'code: {200}'

    except pymysql.Error as e:
        response = {"Status": "ERROR", "reason": f'{e}'}
        return jsonify(response), f'code: {500}'
