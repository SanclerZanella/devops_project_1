from flask import (Blueprint, jsonify, request)
import pymysql
from utils.db_ops import DBOps

# Flask Blueprint
put_method = Blueprint("put_method", __name__)


@put_method.route("/users/<user_id>", methods=["PUT"])
def put_route(user_id):
    """
    Display user from the database
    """

    db_ops = DBOps()

    try:
        user_exist = db_ops.is_user_in_db(user_id)
        if user_exist is False:
            response = {"Status": "ERROR", "reason": "No such ID"}
            return jsonify(response), 500

        data = request.get_json()
        new_value = data.get('user_name')

        db_ops.update_user(user_id, new_value)

        response = {"Status": "OK", "User_updated": f"{new_value}"}
        return jsonify(response), 200

    except pymysql.Error as e:
        response = {"Status": "ERROR", "reason": f'{e}'}
        return jsonify(response), 500
