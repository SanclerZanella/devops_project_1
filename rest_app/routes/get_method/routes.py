from flask import (Blueprint, jsonify, request)
import pymysql
from utils.db_ops import DBOps

# Flask Blueprint
get_method = Blueprint("get_method", __name__)


@get_method.route("/users/<user_id>", methods=["GET"])
def get_route(user_id):
    """
    Display user from the database
    """

    db_ops = DBOps()

    try:
        user_exist = db_ops.is_user_in_db(user_id)
        if user_exist is False:
            response = {"Status": "ERROR", "reason": "No such ID"}
            return jsonify(response), 500

        user = db_ops.retrieve_user(user_id)

        id_user, user_name = user

        response = {"Status": "OK", "User_name": f"{user_name}"}
        return jsonify(response), 200

    except pymysql.Error as e:
        response = {"Status": "ERROR", "reason": f'{e}'}
        return jsonify(response), 500
